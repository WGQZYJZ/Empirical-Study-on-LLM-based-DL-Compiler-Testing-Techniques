
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.add   = torch.ops.quantized.linear.LinearReLUQ(
            80, 768 // 4).float()
 
    def forward(self, x1):
        v1  = self.conv(x1) + self.add(v2) # Add another tensor to the output of the convolution and then apply the ReLU activation function to the result
        return v1


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

