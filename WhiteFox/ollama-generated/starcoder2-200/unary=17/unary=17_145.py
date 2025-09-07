
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.nn.functional.conv_transpose2d(x1, kernel=None)
        v3  = v1 > -0.5
        return v3


# Initializing the model