
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convTranspose  = torch.nn.ConvTranspose2d(3, 8, kernelSize=5)
 
    def forward(self, x1):
        v1  = self.convTranspose(x1) 
        v2  = torch.sigmoid(v1) # This is the modified line
        return v2


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
