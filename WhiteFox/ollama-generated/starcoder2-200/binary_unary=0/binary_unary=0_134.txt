
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x): 
        v0  = self.__constant__ 
        v1  = self.conv(x) + v0 # Apply pointwise convolution to the input tensor and add another constant
        v2  = torch.relu(v1)  # Apply ReLU activation function to the output of the convolution with a different constant
        return v2


# Initializing the model