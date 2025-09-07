
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, 7)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x1):
        v1 = self.conv1(x1) # Apply a convolution with kernel size 7 to the input tensor
        v2 = self.relu(v1)   # Apply the ReLU activation function to the output of the convolution
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
