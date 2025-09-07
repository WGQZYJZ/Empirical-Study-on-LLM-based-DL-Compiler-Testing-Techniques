
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1) # Conv with kernel size 1 and stride 1
        self.relu1 = torch.nn.ReLU()
 
    def forward(self, x1):
        v1 = self.conv1(x1)  # Apply pointwise convolution
        v2 = self.relu1(v1) # Apply the ReLU activation function
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
