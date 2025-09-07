
class Model(torch.nn.Module):
    def __init__(self, dim=3):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(dim, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        x  = x1 + x2
        v1  = self.conv1(x)
        return torch.cat([v1, v1], dim=-1)


# Initializing the model
m  = Model()


