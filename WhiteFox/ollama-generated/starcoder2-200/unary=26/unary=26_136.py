
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.convtranspose = torch.nn.ConvTranspose2d(3, 8, 1)
        self.negative_slope  = negative_slope

    def forward(self, x1):
        v1  = self.convtranspose(x1)
        v2  = v1 > 0 
        v4  = torch.where(v2, v1, -self.negative_slope * v1)
        return v4
        
# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(3, 8, 65, 70)


# Generating the output
__output__  = m(x1)