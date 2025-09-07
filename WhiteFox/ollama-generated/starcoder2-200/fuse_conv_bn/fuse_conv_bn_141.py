
class FusedModel(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # X can be 0 or 3 for convXd
        v1 = torch.nn.functional.conv3d(x1, torch.ones(25)) 
        return v1

# Initializing the model
m  = FusedModel()

# Inputs to the model
x1  = torch.randn(10)

__output__  = m(x1)

