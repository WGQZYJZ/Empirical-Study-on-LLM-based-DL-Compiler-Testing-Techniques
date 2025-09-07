
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.cat = torch.nn.Cat([
            torch.nn.Conv2d(3, 8, 1), 
            torch.nn.Conv2d(3, 8, 1)], dim=1)
 
    def forward(self, x1):
        v1 = torch.cat([x1, x1], dim=1)
        v2 = v1[:, :size]
        v3 = v2[:, :size]
        v4 = torch.cat([v1, v3], dim=1)
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
