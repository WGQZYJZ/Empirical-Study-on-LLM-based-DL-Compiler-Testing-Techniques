
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_mask = torch.eye(3, dtype=torch.float).unsqueeze(dim=0) # Attention mask for the three heads in transformer

    def forward(self, query, key, value):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk = qk + self.attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
        output = attn_weight @ value # Compute the dot product of the dropout output and the value
        return output

# Initializing the model
m = Model()

# Inputs to the model
query  = torch.randn(2, 3, 64, 64)
key    = torch.randn(2, 8, 64, 64)
value  = torch.randn(2, 8, 64, 64)
