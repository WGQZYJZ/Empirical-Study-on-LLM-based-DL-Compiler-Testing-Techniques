
class Model(torch.nn.Module):
    def __init__(self, d_model, nhead, num_buckets=512):
        super().__init__()
        self.d_model = d_model
        self.nhead = nhead
        self.num_buckets = num_buckets
        self.scale = math.sqrt(d_model)

        self.layernorm1 = torch.nn.LayerNorm(self.d_model, eps=1e-6)
        self.layernorm2 = torch.nn.LayerNorm(self.d_model, eps=1e-6)

    def forward(self, x):
        query  = self.scale * torch.sin(x[:, :, :self.num_buckets // 2])
        key     = self.scale * torch.cos(x[:, :, :self.num_buckets // 2])

        key    *= (1 / math.sqrt(self.nhead))  # Scale the keys to have norm 1
        query  *= (1 / math.sqrt(self.nhead))  # Scale the queries to have norm 1
        attn_mask = torch.triu(torch.ones((self.num_buckets, self.num_buckets), device=x.device), diagonal=-1)

        # Compute the dot product of the query and key using softmax function
        qk = (query @ key).softmax(dim=-1)  # QK = Q @ K / sqrt(d_k)
        attn_weight = torch.dropout(qk, dropout_p, True)  # Apply dropout to the softmax output

        value = x[:, :, :self.num_buckets // 2] * math.sin(attn_mask[:, :, :self.num_buckets // 2])

        x1 = torch.cat([value, attn_weight], dim=1)  # X1 = V + A
        x = self.layernorm1(x1)  # X1 = LN(V + A)
        x = F.dropout(x, dropout_p, True)  # Apply dropout to the input x

        return x


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
