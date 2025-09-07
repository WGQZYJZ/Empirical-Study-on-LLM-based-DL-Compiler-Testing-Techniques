
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1)

    def forward(self, x1): 
        v1 = self.conv(x1)  
        v2 = nn.ReLU()(v1)  
        return v2


# Initializing the model
m = Model()
m2=Model2()
 
# Inputs to both models
x  = torch.randn(1,3,64,64)  
x2 = x

# Outputs of each model on different inputs
__output__  = m(x)
__output__2 = m2(x2) 
