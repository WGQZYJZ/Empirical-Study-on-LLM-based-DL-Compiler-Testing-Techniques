

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convTrans  = torch.nn.ConvTranspose2d(3,8,1)
 
    def forward(self, x1):
        v1  = self.convTrans(x1)
        v2  = torch.sigmoid(v1)
 
        return v2

m  = Model()

# Inputs to the model