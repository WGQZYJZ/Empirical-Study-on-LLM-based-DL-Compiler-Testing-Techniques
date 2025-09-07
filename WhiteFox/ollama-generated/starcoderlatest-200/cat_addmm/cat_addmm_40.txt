
class Model(torch.nn.Module):
    def __init__(self, dim = 1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.addmm(v1, torch.tensor([[1]]), torch.eye(v1.shape[0]).type_as(v1))
        v3 = torch.cat([v2], dim=dim)
        return v3


# Initializing the model
m = Model()

