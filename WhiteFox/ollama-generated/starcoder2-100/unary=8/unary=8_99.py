
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.unconv= torch.nn.ConvTranspose2d(4, 6, 5)
 
    def forward(self, x1): 
        v0 = [x1]
        v1  = self.conv(v0[-1]) 
        v1 = F.relu(v1, inplace=False) # Apply ReLU
        v3 = torch.clamp(torch.div(v2,6),min=-5)
        return [v1+3, v3]


# Initializing the model
m  = Model()
 
# Inputs to the model
x0  = m.conv(torch.randn(1, 4, 64, 64)) # input tensor of size (1, 8, 576, 576)
x2  = F.relu(x0, inplace=True)            # ReLU to apply on a given module
x3  = torch.clamp(torch.div(x2,4), min=-10) # clamp operation applied with a given value -10
 