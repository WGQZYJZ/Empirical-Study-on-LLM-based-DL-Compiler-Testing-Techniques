
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1).float() # To avoid precision issue on the GPU, use float instead of double-precision floating point number

        ## The below line will create an error if we don't change it, which indicates that t4 must be a half type
        v2 = torch.cumsum(v1, 1) # Compute the cumulative sum of the elements of the tensor along dimension 1
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
