
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, kernel_size=1)
 
    def forward(self, x):
        return self.conv(x)
 
 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.activation = torch.nn.Sigmoid()
    
    def forward(self,  x):
        return self.activation(x)


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)


