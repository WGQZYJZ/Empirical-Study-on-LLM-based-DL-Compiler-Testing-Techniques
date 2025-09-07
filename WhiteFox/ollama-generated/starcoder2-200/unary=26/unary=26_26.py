
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convTranspose  = torch.nn.ConvTranspose2d(3, 8, kernelSize=1)
 
    def forward(self, x1):
        v1  = self.convTranspose(x1)
        v2  = (v1 > 0).type_as(v1) # Create mask based on threshold value in this case it is 0
        v3  = negative_slope * v1
        v4  = torch.where(v2, v1, v3) 
        return v4


# Initializing the model