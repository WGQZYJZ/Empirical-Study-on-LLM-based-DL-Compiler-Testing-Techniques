
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2578134986457825):
        super().__init__()
        self.convt  = torch.nn.ConvTranspose2d(32, 8, 1)
        self.negative_slope  = negative_slope
 
    def forward(self, x1):
        v1  = self.convt(x1)
        v2  = v1 > 0
        v3  = v1 * -0.5764398497998718 # Negative Slope
        v4  = torch.where(v2, v1, v3)
 
        return v4


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(10, 32, 64, 64) # Input tensor of shape (batch_size, num_channels, height, width). 

# __output__ is a tensor that represents the output of the model when given inputs `x1`.