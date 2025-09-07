
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(3, 8)
 
    def forward(self, q1, k1, v1):
        attn_weight = self.attn(q1, k1, v1)[0]
        output = attn_weight @ v1
        return output

# Initializing the model
m = Model()

# Inputs to the model
q1 = torch.randn(32, 3, 64, 64)
k1 = torch.randn(32, 3, 64, 64)
v1 = torch.randn(32, 3, 64, 64)
