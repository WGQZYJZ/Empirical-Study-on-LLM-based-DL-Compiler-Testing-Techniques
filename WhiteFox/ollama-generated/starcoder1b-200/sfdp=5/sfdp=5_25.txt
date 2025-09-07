
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v = self.conv(x1)
        return torch.softmax(v, dim=-1) @ v


# Initializing the model
m = Model()

