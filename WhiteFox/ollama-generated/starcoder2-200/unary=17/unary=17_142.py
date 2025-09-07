
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.convT = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x):
        v0= x
        v1  = v0 * 5
        v4 =  v1 / v4
        v6  = self.convT(v7)
        return v6

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 20, 15)

 # The first output of the model is the model without activation function and without dropout
__output__  = m(x1).squeeze(-1).squeeze(-1)


