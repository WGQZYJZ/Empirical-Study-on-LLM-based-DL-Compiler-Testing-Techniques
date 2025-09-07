
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = F.sigmoid(v1) # Applies the sigmoid function element-wise to the input tensor
        v3  = v1 * v2  # Multiplies the input of the convolution with the output of the sigmoid function
        return v3


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

