
class Model(torch.nn.Module):
    def __init__(self, constant=0.5):
        super().__init__()
        self.constant = constant
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2  = v1 - self.constant # Subtract 'other' from the output of the convolution
        return v2


# Initializing the model and set the constant to be a random float between 0.5 and 3.9, and then set the random seed for reproducibility (see [torch.manual_seed()](https://pytorch.org/docs/stable/generated/torch.manual_seed.html))
random.seed(1) # Setting a fixed random seed for reproducability
m = Model(constant=random.uniform(0.5, 3.9))


# Inputs to the model (see [torch.randn()](https://pytorch.org/docs/stable/generated/torch.randn.html) and [torch.normal()](https://pytorch.org/docs/stable/generated/torch.normal.html)) for a random tensor with shape of 1 x 3 x 64 x 64
x1 = torch.randn(1, 3, 64, 64)


__output__  = m(x1)
