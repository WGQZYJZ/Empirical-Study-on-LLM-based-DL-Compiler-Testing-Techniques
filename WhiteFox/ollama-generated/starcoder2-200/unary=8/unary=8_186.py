
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.convT(x1)
        v2  = v1 + 3 # add 3 to the transposed convolution output
        v3  = torch.clamp(v2, min=0) # clamp the output of the addition operation to a minimum of 0 
        v4  = torch.clamp(v3, max=6) # clamp the output of the previous clamp operation to a maximum of 6
        v5  = v1 * v4 # multiply the transposed convolution output by the output of the clamp operation 
        v6  = v5 / 6 # divide the multiplication operation by 6
        return v6

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(2,3,64,64)
