
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, kernel_size=(1, 4), stride=(1, 2))
        self.relu  = torch.nn.LeakyReLU(negative_slope=negative_slope)
 
    def forward(self, x):
        v  = self.conv(x)
        v2 = self.relu(v)
        return v2


# Initializing the model
m  = Model()


