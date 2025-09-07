
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, qk, attn_mask):
        v1 = torch.matmul(qk, key.transpose(-2, -1) / math.sqrt(query.size(-1)))
        v2 = v1 + attn_mask
        output = torch.softmax(v2, dim=-1) @ value
        return output


# Initializing the model
m = Model()

# Inputs to the model
qk = torch.randn(batch_size, query.size(-1), key.size(-2))
attn_mask = torch.ones_like(v1)
