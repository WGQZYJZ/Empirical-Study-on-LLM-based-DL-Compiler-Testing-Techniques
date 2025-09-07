
class Model(torch.nn.Module):
    def __init__(self, negative_slope=1.):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
        self.relu  = torch.nn.LeakyReLU(negative_slope=negative_slope)
 
    def forward(self, x):
        v1  = self.conv(x)
        v2  = self.relu(v1)
        return v2


# Initializing the model
m = Model()


