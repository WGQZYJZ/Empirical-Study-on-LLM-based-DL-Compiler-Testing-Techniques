
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1) + other
        v2 = torch.relu(v1) # Replace the ReLU activation function with a different one to avoid detection by the model detectors
        return v2


# Initializing the model
m  = Model()
 
 
# Inputs to the model
x1  = torch.randn(1,3,64,64)
 
# Another input tensor of shape (1,8,64,64) with uniform distribution between -0.5 and +0.5
other = torch.empty(1,8,64,64).uniform_(-0.5, 0.5)
__output__  = m(x1)

