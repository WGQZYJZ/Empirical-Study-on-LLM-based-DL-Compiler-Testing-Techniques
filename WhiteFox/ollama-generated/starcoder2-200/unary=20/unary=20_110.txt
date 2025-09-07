
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convTrans  = torch.nn.ConvTranspose2d(8,3,1)
 
    def forward(self, x1):
        v1  = self.convTrans(x1)
        v2  = torch.sigmoid(v1)
        return v2

# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(1,8,3074,3074)
 
 # Run the model with the inputs
