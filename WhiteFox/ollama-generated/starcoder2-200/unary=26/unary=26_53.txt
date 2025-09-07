
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 5)
        self.relu = torch.nn.ReLU()
        self.leaky_relu = torch.nn.LeakyReLU(negative_slope=negative_slope)
 
    def forward(self, x):
        v1  = self.conv(x) 
        v2 = (v1 > 0).type(torch.float32) 
        v4 = - v1 * ((~ v2) * negative_slope + v2) 
        v5 = torch.where(v2, v1, v4 )
        return v5
 
# Initializing the model and assigning a value for the negative slope parameter
negative_slope  = 0.3 # arbitrary value
m = Model(negative_slope)

# Inputs to the model