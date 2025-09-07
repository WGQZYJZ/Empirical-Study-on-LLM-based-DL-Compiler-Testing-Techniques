
class Model(torch.nn.Module):
    def __init__(self, inp):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = v1 + inp
        return v2


# Initializing the model
inp = torch.randn(3072, dtype=torch.float32)  # input tensor is different from the previous one
m = Model(inp)

# Inputs to the model
x1 = torch.randn(5, 64, 64)
x2 = torch.randn(64, 64)
