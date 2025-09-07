
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3,8, 5)
        self.conv2 = torch.nn.Conv2d(3,4, 7)
 
    def forward(self, x):
        v0 = 6 * 1 + (x ** 3).mean() - ((x ** 3)).mean()
        v1  = self.conv1(v0) # Apply a pointwise convolution to the input tensor. Please specify the size of kernel as '5'.
        v2  = torch.relu(self.conv2(torch.tanh(x)))  + 3 # Apply another convolution, this time pointwise and then applying a non-linearity such as tanh or ReLU on it
        return v1 * 0.8697452 - x * 1
# Initializing the model:
m = Model()
 
# Inputs to the model
x  = torch.randn(3, 3, 64, 64)

