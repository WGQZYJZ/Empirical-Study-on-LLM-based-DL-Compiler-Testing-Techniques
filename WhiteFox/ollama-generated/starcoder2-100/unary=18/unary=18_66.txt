
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        v1 = conv(x)
        v2 = torch.sigmoid(v1) # Add your code here
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x  = torch.randn(1,3,64,64)
__output__  = m(x)

- The outputs of each layer should be a float with the value in the range [0; 1]
- There shouldn't exist any layers that are not fully connected layers

