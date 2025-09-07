
class Model(torch.nn.Module):
    def __init__(self, conv):
        super().__init__()
        self.conv = conv
 
    def forward(self, x1, other=None):
        v1  = self.conv(x1)
 
        return v1 + other
 
# Initializing the model with a given convolutional layer as an argument
conv_layer  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
m  = Model(conv_layer)
 
 
# Inputs to the model. This input tensor does not have shape [None, None], so it will be added as an argument to the function.
x1  = torch.randn(1, 3, 64, 64)
 
# Running the model with the inputs and the keyword arguments. We provide a new "other" tensor here.
__output__  = m(x1, other=torch.randn(10))

