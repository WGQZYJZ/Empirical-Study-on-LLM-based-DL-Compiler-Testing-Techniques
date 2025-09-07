
class Model(torch.nn.Module):
    def __init__(self, min_value=1e-10, max_value=1e+10):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return v1 - min_value


# Initializing the model
m = Model(min_value=-1e-10, max_value=1e+10)


