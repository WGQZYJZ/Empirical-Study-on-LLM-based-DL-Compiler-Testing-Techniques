
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, kernel_size=1, stride=2)
        self.lrelu = torch.nn.LeakyReLU(negative_slope=0.01)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = self.lrelu(v1)
        return v2


# Initializing the model
m = Model()


