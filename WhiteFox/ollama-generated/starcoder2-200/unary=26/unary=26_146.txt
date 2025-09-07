
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.nn.functional.conv_transpose2d(x1, 3)
        return v1

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(64, 8, 500, 500)
