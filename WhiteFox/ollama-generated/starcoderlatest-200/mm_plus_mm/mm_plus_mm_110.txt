
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x3, x4)
        v3 = v1 + v2
        return v3


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(800, 1596, dtype=torch.float32).contiguous()
x2 = torch.randn(720, 1440, dtype=torch.float32).contiguous()
x3 = torch.randn(1440, 672, dtype=torch.float32).contiguous()
