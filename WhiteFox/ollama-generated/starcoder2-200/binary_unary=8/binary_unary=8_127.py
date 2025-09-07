
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = self.conv(x1) # Pointwise conv
        v2  = v1 + other 
        return torch.relu(v2) # ReLU activation function

# Initializing the model
m  = Model()

 # Inputs to the model 
other = torch.randn(1, 3, 64, 64) # Another tensor
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)