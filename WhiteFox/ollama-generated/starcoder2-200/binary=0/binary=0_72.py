
class Model(torch.nn.Module):
    def __init__(self, m):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, m):
        v1  = self.conv(x1)
        return v1 + m


# Initializing the model with an argument
m = Model(torch.ones(1))
 
 # Inputs to the model
 x1 = torch.randn(1, 3, 64, 64)
 