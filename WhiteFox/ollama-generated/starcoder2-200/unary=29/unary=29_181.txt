
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3,8,1)
    
    def forward(self, x):
        v1 = conv_(x)
        return torch.clamp_min(v1, min_value)


# Initializing the model
m  = Model()


# Inputs to the model
x1= torch.randn(100,3,64,64)
__output__  = m(x1)

