
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, kernel_size=1)
 
    def forward(self, x):
        v1 = self.convT(x)
        v2 = F.sigmoid(v1)
        v3 = v1 * v2
        return v3


# Initializing the model
m = Model()

 # Inputs to the model
x  = torch.randn(1, 3, 64, 64)
 
