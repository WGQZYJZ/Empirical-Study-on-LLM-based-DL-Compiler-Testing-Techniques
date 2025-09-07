
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convtrans = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
 
    def forward(self, x1):
        v1  = self.convtrans(x1)
        v2  = torch.sigmoid(v1)
        v3  = v1 * v2 
        return v3


# Initializing the model
m  = Model()

 # Inputs to the model 
 x1  = torch.randn(1, 8, 64, 64)
 
 # Outputs from the model
__output__  = m(x1)

