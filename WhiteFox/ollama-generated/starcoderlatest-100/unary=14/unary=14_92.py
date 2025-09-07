
class GLUModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.nn.functional.conv_transpose2d(x1, 8, 64, stride=2)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        return v3


# Initializing the model
m = GLUModel()

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
