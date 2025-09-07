
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = self._conv1
        v1  = self._conv2
        v2  = torch.relu(v1 + other) # The ReLU activation function is added to the output of a pointwise convolution
        return v2


# Initializing the model