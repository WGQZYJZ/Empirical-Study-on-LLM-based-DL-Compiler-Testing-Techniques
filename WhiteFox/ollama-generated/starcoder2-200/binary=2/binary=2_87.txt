
class Model(torch.nn.Module):
    def __init__(self, input=3):
        super().__init__()
        self.conv = torch.nn.Conv2d(input, 8, kernel_size=(1), padding='same')
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other
        return v2


# Initializing the model with input value as 3 instead of default 5 in Model's __init__ method.
m = Model(input=3)


# Inputs to the model
x1 = torch.randn(4, 3, 608, 799).to("cuda") # Input with shape [batch_size x channel x height x width].
other = torch.randn(4, 5, 254, 254) # other could be a scalar or an arbitrary tensor of the same shape as the output of the convolution.
