
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.convT  = torch.nn.ConvTranspose2d(3,8,1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1  = self.convT(x1) # Apply the transposed convolution to input tensor x1
        mask = v1 > 0 # Create a mask where each element is True if the corresponding element in v1 is greater than 0
        v2  = v1 * -self.negative_slope # Multiply by the negative slope
        v3  = torch.where(mask,v1,v2) # Select elements from v1 or v2 based on mask
        return v3


# Initializing the model
m = Model()


# Inputs to the model: x1
x1 = torch.randn(1, 3, 64, 64)


__output__  = m(x1) # The output of applying the forward function is not zero because the mask contains True values

