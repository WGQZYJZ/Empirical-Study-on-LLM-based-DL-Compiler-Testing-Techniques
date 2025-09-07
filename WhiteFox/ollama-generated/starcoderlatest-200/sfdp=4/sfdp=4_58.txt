
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.key = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, qk):
        query, key = qk[..., :1], qk[..., 1:]
 
        v  = (query @ self.key.transpose(-2, -1) / math.sqrt(query.size(-1))) + attn_mask  # compute attention weights
        output  = torch.softmax(v, dim=-1)  # apply softmax to the result
        output = output @ value # apply dot product

        return output


# Inputs to the model
qkv = torch.randn(2, 3, 64, 64)
qk = qkv[..., :1]
kvt = torch.randn(2, 8, 64, 64)
value = kvt
