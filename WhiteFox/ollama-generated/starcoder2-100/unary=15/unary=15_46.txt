
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.relu  = torch.nn.ReLU()
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v400  = self.relu(v1) # Insert a new ReLU activation function between the convolution layer and the output of the model
        return v400


# Initializing the model
m  = Model()
 
# Inputs to the model
x1   = torch.randn(1, 3, 64, 64)
 
__output__  = m(x1)
 
 