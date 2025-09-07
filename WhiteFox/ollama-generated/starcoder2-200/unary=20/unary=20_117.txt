
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convTrans = torch.nn.ConvTranspose2d(3, 8, kernel_size=1)
 
    def forward(self, x):
        v1  = self.convTrans(x)
        v2  = torch.sigmoid(v1)
        return v2


# Initializing the model
m = Model()
 
 # Inputs to the model
x  = torch.randn(30, 64, 57, 93)

 