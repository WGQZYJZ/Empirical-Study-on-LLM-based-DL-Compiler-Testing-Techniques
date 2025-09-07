
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.convTranspose = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x):
        v0 = self.convTranspose(x) 
        v1  = torch.sigmoid(v0) 
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(32, 49, 6, 8) 

