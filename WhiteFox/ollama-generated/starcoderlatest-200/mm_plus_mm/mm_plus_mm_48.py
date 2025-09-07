
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
x1 = torch.randn(64, 64) # Shape: (64, 64), minval: -0.59999976, maxval: 0.59999982
x2 = torch.randn(64, 64) # Shape: (64, 64), minval: -0.59999976, maxval: 0.59999982
x3 = torch.randn(128, 64) # Shape: (128, 64), minval: -0.59999976, maxval: 0.59999982
x4 = torch.randn(64, 128) # Shape: (64, 128), minval: -0.59999976, maxval: 0.59999982
