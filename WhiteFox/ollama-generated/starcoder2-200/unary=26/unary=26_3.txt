
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.15):
        super().__init__()
        self.convT  = torch.nn.ConvTranspose2d(3,8,1)
        self.negative_slope  = negative_slope

    def forward(self, x1):
        v1  = self.convT(x1)

        mask  = (v1 > 0).float() # Create a mask where each element is True if the corresponding element in t1 is greater than 0 and False otherwise

        v2  = v1 * negative_slope 

        v3  = torch.where(mask, v1, v2) # Apply the where function to select elements from v1 or v2 based on the mask
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)