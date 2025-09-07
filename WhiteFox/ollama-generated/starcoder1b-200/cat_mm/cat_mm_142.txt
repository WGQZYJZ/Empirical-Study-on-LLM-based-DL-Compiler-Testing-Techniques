
class Model(torch.nn.Module):
    def __init__(self, dim=3):
        super().__init__()
        self.conv = torch.nn.Conv2d(dim, 16, 1)
 
    def forward(self, x1):
        return torch.cat([x1 + 0.5, x1 + 0.7], dim=-1)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 128, 128)
