
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = torch.nn.functional.conv3d(x1, weight=None) # No batch normalization layer is used as input for conv2d
        return v

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(4, 50, 60, 70)
__output__  = m(x1)

