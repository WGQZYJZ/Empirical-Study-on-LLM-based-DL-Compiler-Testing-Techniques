
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, other):
        v1  = self.conv(x1)
        v2  = v1 + other # v1 + other: output of conv + the keyword argument value "other" 
        return v2


# Initializing the model with a new input tensor to test.
m_2  = Model()
m_2.__setattr__('conv', torch.nn.Conv2d(3,8,3)) # A new convolution layer
x1 = torch.randn(10,4,64,64) # Input tensor with new dimensions
x2 = torch.randn(10,5, 32, 32) # An input to test different sizes of a new tensor

__output_2  = m_2(x1, x2)
