
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.add = torch.add
        self.relu = torch.nn.ReLU()
 
    def forward(self, x1):

        v1  = self.conv(x1)
 
        v2  = self.add(v1, other)
        v3  = self.relu(v2)
        
        return v3


# Initializing the model
m = Model()


# Inputs to the model
other  = torch.randn(10,) # Randomly generate another tensor to be added to the output of the convolution operation
x1  = torch.randn(5, 8, 64, 64)
__output__  = m(x1)

