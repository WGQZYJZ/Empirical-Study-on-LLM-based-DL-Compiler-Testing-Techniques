
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other
        return v6


# Initializing the model
m = Model()

# Inputs to the model
other = torch.randn(8, 3, 4, 4) # shape (8, 3, 4, 4)
x1 = torch.randn(1, 3, 64, 64)
