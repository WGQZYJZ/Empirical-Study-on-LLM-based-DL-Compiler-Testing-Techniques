
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Transposed convolution operation with kernel size of 1 
        v2  = v1 + 3         # Addition operation by a constant 3 to the output of the transposed convolutional layer
        v3  = torch.clamp_min(v2, 0)# Clamping at minimum of 0 in the previous operation result
        v4  = torch.clamp_max(v3, 6) # Clamping at maximum of 6 in the previous operation result
        v5  = v4 / 6          # Divide by 6 in the previous operation result
        return v5

# Initializing the model with different parameters from the previous model
m2 = Model()


# Inputs to the model m2