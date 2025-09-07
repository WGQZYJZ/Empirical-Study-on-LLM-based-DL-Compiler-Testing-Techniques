
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        v1 = self.conv(x)
        return torch.sigmoid(v1)

# Initializing the model
m = Model()


# Inputs to the model