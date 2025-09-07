
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(8,3,1)
 
    def forward(self, x1):
        v1  = self.convT(x1)
        v2  = torch.sigmoid(v1)
        v3  = v1 * v2 
        return v3

# Initializing the model with different initialization methods compared to previous model
m  = Model()


# Inputs for the model
__input1__  = torch.randn(1,8,56,56)
__output1__  = m(__input1__) 

