
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, other=None):
        v1 = self.conv(x1)
        if other is not None:
            v2 = v1 + other
        else:
            v2 = torch.relu(v1)
        return v2


# Initializing the model
m = Model()

 # Inputs to the model and their respective keywords in the function call
 x1 = torch.randn(1, 3, 64, 64)
 v1 = m(x1, other=torch.randn(1))
