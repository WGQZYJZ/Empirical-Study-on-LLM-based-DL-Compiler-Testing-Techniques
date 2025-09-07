
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Convolution
        v2  = v1 + other   # Addition
        v3  = torch.relu(v2)# Activation Function
        return v3


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
other = x1.clone().detach().requires_grad_(True) # other is a copy of input and requires gradient

