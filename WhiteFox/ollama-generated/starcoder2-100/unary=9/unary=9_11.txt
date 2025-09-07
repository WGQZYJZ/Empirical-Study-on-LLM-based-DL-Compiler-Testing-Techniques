
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
    
    def forward(self, x1):
        v1 = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2 = v1 + 3 # Add 3 to the output of the convolution
        v3 = torch.clamp_min(v2, 0) # Clamp the result of the addition operation to a minimum of 0
        v4 = torch.clamp_max(v3, 6) # Clamp the previous result of clamping to a maximum of 6
        v5 = v4 / 6 # Divide the output by 6 to scale back to the original range
        return v5

# Initializing the model
m1 = Model()


# Inputs to the model 1
x1  = torch.randn(1, 3, 28, 28)


