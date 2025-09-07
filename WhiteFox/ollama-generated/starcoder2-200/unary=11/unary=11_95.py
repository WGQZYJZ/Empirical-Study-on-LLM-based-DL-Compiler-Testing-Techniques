
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, 1)

    def forward(self, x1):

        v1 = self.conv(x1)
        v2 = v1 + 3 # Add 3 to the output of the transposed convolution
        v3 = torch.clamp_min(v2,0) # Clamp at minimum 0
        v4 = torch.clamp_max(v3,6) # Clamp max is 6 
        v5 = v4/6 # Divide by 6
        return v5


# Initializing the model
m = Model()
 

# Inputs to the model
x1  = torch.randn(1,8,64,64)
  