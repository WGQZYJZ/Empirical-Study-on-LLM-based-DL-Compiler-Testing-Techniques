
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = v1 + other # Adding another tensor to the output of a pointwise convolution
        return v2.relu()


# Initializing the model
m  = Model()


# Inputs to the model
other = torch.randn(3, 8, 64, 64)
x1   = torch.randn(1, 3, 64, 64)


# Output of the model
__output__  = m(x1)

