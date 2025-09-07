
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv  = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=0)

    def forward(self, x1):
        v1  = self.deconv(x1)
        v2  = v1 * 0.5
        v3  = v2  * v2 * v2 
        v4  = torch.sigmoid(v3)
        v6  = v4 + v4  
        return v6

 # Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 8, 50, 50)
