
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convTrans = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
        self.activation = torch.nn.ReLU()
 
    def forward(self, x1):
        v1  = self.convTrans(x1)
        return self.activation(v1)

# Initializing the model
m = Model()

# Inputs to the model
x2 = torch.randn(1, 3, 40, 65)
__output_2__  = m(x2)

