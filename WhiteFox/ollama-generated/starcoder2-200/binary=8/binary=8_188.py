
class Model(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other = kwargs["other"]
 
    def forward(self, x1):
        v1  = self.conv(x1)
        return v1 + self.other


# Initializing the model with keyword argument: other
m = Model(other = torch.zeros([8]))

# Inputs to the model: passing one argument (x1 in this case) and one keyword argument ("other" set to "zero tensor")

x1  = torch.randn(1, 3, 64, 64)
