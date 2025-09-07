
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
 
    def forward(self, x1, min_value=-0.5, max_value=1.5):
        v1 = self.conv(x1)
        return v1


# Initializing the model
m = Model()


