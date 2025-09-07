
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1=None):
        v1 = self.conv2d(x1) # Apply pointwise convolution with kernel size 3 to the input tensor
        v4_sum = torch.addmm(y1, self.conv2d.weight) # Apply a 3D-tensor matrix multiplication between an input and the weight of another pointwise convolution layer
        v7 = 5 * x1 + y1 - v1 
        v8 = (v1 - x1) / v4_sum
        v9 = torch.div(x1, self.conv2d(y1)) # Apply a division between an input and the output of another pointwise convolution layer
        return v7, v8, v9


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1,3,64,64)
x2 = x1 * -0.5 + 0.5 #  Adding a constant tensor  (specified by the keyword argument "other") to another tensor (specified by the keyword argument y1). Note that, this operation is equivalent to dividing the input tensor with another pointwise convolution layer’s weight
y2 = torch.randn(64)
__output__, __output_1__, __output_2__  = m(x1, x2)

