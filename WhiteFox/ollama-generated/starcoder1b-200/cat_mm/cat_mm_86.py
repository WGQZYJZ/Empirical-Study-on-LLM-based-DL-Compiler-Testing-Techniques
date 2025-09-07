
class Model(torch.nn.Module):
    def __init__(self, cat_dim=1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = v1 * 0.5 + x2
        return torch.cat([v1, v2], dim=cat_dim)


# Initializing the model
m = Model()


