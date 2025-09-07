
class Model(torch.nn.Module):
    def __init__(self, input1, input2=None):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + input2  # Adding another tensor to the output of a convolution
        return v2

# Initializing the model with passing an argument to the addition operation
m  = Model(torch.randn(1,3,64,64), torch.randn(1,8,50,79))

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)


