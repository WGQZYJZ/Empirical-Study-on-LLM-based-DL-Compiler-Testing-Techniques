
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x):
        v = torch.full([arg1, arg2], 1)
        return v


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
