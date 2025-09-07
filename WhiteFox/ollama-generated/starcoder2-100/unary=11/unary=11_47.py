
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvTranspose2d(8, 3, kernel_size=1, stride=1)
 
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = v1 + 3
        v3 = torch.clamp(v2, min=-0.5, max=6)
        v4 = torch.div(v3, 6.)
        return v4


# Initializing the model
m = Model()


# Inputs to the model