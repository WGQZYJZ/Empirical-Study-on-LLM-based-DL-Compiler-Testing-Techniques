
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1) > 0 # Create a boolean mask for the output of the convolution based on the threshold value zero
        v2 = v1 * -1e-4 # Set the negative_slope parameter to 0.0001 if elements in t1 are greater than 0, else set it to 0
        v3 = torch.where(v1, v1, v2) # Select each element of the output of the convolution using a mask based on the threshold value zero (if selected with 0 otherwise -1e-4).
        return v3


# Initializing the model
m  = Model()
# Inputs to the model
x1 = torch.randn(2, 8)
__output__= m(x1) 
