
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, other):
        v1 = self.conv(x1)
        v2 = v1 + other
        return v2


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(1, 3, 64, 64) # Input tensor for the first convolution layer in the model
other = torch.randn(1, 3, 80, 80) # Input tensor for the second convolutional layer
 
# Calling the forward method on the model with inputs x1 and other as keywords
__output__  = m(x1=x1, other=other)

