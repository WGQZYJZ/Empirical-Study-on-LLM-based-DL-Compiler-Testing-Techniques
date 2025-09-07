
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Convolutional layer
        v2  = v1 > 0         # Boolean mask
        v3  = v1 * negative_slope 
        v4  = torch.where(v2, v1, v3 )   
        return v4

# Initializing the model with a given negative slope value
negative_slope  =  0.5


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64) 

# Running the model
__output__  = m(x1)
