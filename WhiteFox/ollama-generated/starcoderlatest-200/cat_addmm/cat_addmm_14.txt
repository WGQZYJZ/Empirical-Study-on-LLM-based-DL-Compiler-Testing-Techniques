
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = x1
        v2 = torch.addmm(v1, torch.eye(x1.shape[1]), torch.eye(x1.shape[2]))
        v3 = torch.cat([v2], dim=0)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
