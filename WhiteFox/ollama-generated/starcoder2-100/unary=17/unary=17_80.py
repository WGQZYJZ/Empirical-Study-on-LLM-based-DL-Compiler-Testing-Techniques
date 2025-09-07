
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v1  = convT(x1)
        return relu(v1)
# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(1,8,64,32)
 
 __output__  = m(x1)
 