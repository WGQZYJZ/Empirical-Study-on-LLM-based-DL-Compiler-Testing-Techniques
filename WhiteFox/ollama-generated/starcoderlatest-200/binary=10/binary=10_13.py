
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv = torch.nn.Linear(128, 512)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other
        return v2


# Initializing the model
m = Model()
other_tensor = torch.randn(10)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
