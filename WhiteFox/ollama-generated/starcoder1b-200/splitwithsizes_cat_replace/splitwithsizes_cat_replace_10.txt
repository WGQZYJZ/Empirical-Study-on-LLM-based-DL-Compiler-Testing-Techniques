
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        return torch.split(x1, [0.5, 0.7071], dim=-1)[0]


# Initializing the model
m = Model()


