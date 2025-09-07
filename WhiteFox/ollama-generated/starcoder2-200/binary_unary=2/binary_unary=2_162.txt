
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1): 
        v1  = self.conv(x1)

        v5  = (v1 - other).clamp_min_(0.) # Apply the ReLU activation function
        return v5

# Initializing model
m  = Model()


# Inputs to the model
x1   = torch.randn(2, 3, 64, 64) # A random input tensor
other  = (torch.rand_like(x1)-0.5)*0.7
__output__  = m(x1)

