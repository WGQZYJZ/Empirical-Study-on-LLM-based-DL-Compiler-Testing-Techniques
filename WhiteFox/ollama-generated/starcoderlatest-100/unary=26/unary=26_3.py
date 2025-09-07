
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.01):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 4, stride=1, padding=2)
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 16, stride=4, padding=2)
        self.negative_slope = negative_slope
 
    def forward(self, x):
        t1 = self.conv_transpose(x) # Apply pointwise transposed convolution to the input tensor
        t2 = t1 > 0
        t3 = t1 * self.negative_slope
        t4 = torch.where(t2, t1, t3)
        return t4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
