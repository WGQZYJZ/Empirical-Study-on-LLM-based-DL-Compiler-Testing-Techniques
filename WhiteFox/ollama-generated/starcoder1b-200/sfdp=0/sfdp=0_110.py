
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1)
        self.linear  = torch.nn.Linear(16 * 7 * 7, 1)
 
    def forward(self, x):
        # Apply pointwise convolution with kernel size 1 to the input tensor
        v1  = self.conv1(x).view(x.shape[0], -1)
        v2  = v1  * 0.5
        v3  = v1  * 0.7071067811865476
        # Apply pointwise convolution with kernel size 1 to the output of the first layer (conv1), and apply the error function to the output of the second layer (conv2)
        v4  = torch.erf(v3).view(x.shape[0], -1)
        v5  = v4  + 1
        # Apply pointwise convolution with kernel size 1 to the output of the first and second layers, and apply the error function to the sum of the outputs (conv2 + conv1)
        v6  = v2  * v5
        return v6

# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(1, 3, 64, 64)
