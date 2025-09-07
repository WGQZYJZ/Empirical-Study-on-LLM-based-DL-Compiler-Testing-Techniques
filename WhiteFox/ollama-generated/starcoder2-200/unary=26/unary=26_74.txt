
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        mask  = (v1 > 0).float() # mask: True if value is greater than zero otherwise False
        v4  = torch.where(mask, v1 * -2., v3 * -1.)
        return v6


# Initializing the model
negative_slope  =  5.9784e-09 # a randomly generated negative slope for the operation torch.where in this example
m  = Model(negative_slope)

# Inputs to the model
x2  = torch.randn(1, 3, 64, 64)


