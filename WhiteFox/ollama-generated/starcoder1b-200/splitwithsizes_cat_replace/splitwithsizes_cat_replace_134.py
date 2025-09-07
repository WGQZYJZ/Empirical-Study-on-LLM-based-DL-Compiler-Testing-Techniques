
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10):
        v1 = self.conv(x1)
        v2 = self.conv(v1)  # Apply the first convolution to the input tensor
        v3 = self.conv(x2)
        v4 = self.conv(v3)  # Apply the second convolution to the output of the first convolution
        v5 = self.conv(x3)
        v6 = self.conv(v5)  # Apply the third convolution to the input tensor
        v7 = self.conv(x4)
        v8 = self.conv(v7)  # Apply the forth convolution to the output of the first convolution
        v9 = self.conv(x5)
        v10 = self.conv(v9)  # Apply the fifth convolution to the input tensor
        return v10


# Initializing the model
m = Model()


