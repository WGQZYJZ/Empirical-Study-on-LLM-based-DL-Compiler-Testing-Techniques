class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        v1  = self.conv(x) # Apply pointwise convolution with kernel size 1 to the input tensor
        v4  = sigmoid(v1) # Apply the sigmoid function to the output of the convolution
        v5  = t1 * v2
        return v3
