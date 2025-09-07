
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)

    def forward(self, x): 
        v1 = self.conv(x) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2 = v1 + 3 # Add 3 to the output of the convolution operation
        v3 = torch.clamp_min(v2,0) # Clamp the output of the addition operation to a minimum of 0
        v4 = torch.clamp_max(v3,6) # Clamp the output of the previous operation to a maximum of 6 
        return (v4/6) # Divide the output of the previous operation by 6

# Initializing the model
m = Model()

