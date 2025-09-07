
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3,8,1,stride=1,padding=0)
 
    def forward(self, x1):
        v1  = self.convT(x1) 
        v2  = torch.sigmoid(v1)
        v3  = v1 * v2
        return v3


# Initializing the model and defining the input to the model
m = Model()
 
x1 = torch.randn(8, 3, 64, 64)
