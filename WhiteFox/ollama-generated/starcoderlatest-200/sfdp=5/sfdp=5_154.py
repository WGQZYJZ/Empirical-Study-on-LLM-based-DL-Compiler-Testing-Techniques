
class Model2(torch.nn.Module):
    def __init__(self, attn_size):
        super().__init__()
        self.attn_proj = torch.nn.Linear(attn_size, attn_size)
 
    def forward(self, query, key, value, attn_mask):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
        output = attn_weight @ value
        return output


# Initializing the model
m2 = Model2(attn_size=512)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
query = torch.randn(2, 8, 64, 64)
key   = torch.randn(2, 8, 64, 64)
value = torch.randn(2, 8, 64, 64)
