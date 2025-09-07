
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_mask = torch.eye(6, 6)
 
    def forward(self, query, key, value):
        qk = (query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))) + self.attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ value
        return output

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
x2 = torch.randn(4, 8, 64, 64)
