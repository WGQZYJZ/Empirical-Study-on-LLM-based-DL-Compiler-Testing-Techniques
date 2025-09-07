
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.convT  = torch.nn.ConvTranspose2d(3,8,1,stride=1,padding=1)

    def forward(self, x1):
        v1  = self.convT(x1)
        v2  = v1 > 0 
        v3  = v1 * negative_slope
        v4  = torch.where(v2 , v1, v3) # Use torch.where to select elements from t1 or v3 based on the mask
        return v4

# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 3,64,64)
__output__  = m(x1)