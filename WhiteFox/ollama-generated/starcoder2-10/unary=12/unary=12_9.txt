
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.relu  = torch.nn.ReLU()
 
    def forward(self, x):
        v1 = self.conv(x) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2 = self.relu(v1)# Pass through ReLU activation function
        v3 = v1 * v2# Multiply the output of the convolution by the output of the ReLU activation function
        return v3


# Initializing the model