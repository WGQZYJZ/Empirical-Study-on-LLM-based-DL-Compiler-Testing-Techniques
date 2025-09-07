
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, -0.5)
        v3  = torch.clamp_max(v2, 0.5)

        return v3


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

# Model: A single fully connected layer network. The input size is `784` (size of MNIST input). The number of hidden units for the output layer is provided as a keyword argument in the `__init__` method. The output of this network is also provided using the `return_value` parameter.

class FCModel(torch.nn.Module):
    def __init__(self, inputSize = 784 , outputSize = 512):
        super().__init__()
        self.fc   = torch.nn.Linear(inputSize, outputSize)
    
    def forward(self, x1, return_value=None):
        # The input for this model should be the MNIST dataset
        