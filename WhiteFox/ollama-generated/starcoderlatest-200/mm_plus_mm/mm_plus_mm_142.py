
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3, x4):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x3, x4)
        v3 = v1 + v2
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(256, 64, 7, 7) # input_size=64*7*7
x2 = torch.randn(256, 32, 14, 14) # input_size=32*14*14
x3 = torch.randn(256, 16, 28, 28) # input_size=16*28*28
x4 = torch.randn(256, 8, 56, 56) # input_size=8*56*56
