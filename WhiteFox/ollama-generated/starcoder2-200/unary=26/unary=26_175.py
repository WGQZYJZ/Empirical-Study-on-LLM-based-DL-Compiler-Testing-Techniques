
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 4)
        self.actv   = torch.nn.LeakyReLU()
 
    def forward(self, x):
        v1  = self.conv(x)
        mask  = v1 > 0
        v2  = negative_slope * v1
        v3  = v1 - v2 
        v4  = torch.where(mask, v1, v2) # This pattern is for a Leaky ReLU
        return v4

# Initializing the model
m  = Model()


# Inputs to the model
x = torch.randn(10,3,64,64)
