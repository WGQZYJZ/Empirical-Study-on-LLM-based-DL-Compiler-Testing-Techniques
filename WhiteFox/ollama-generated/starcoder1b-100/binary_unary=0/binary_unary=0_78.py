
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) + torch.randn_like(v1) * 0.5
        return torch.relu(v1)


# Initializing the model
m = Model()

