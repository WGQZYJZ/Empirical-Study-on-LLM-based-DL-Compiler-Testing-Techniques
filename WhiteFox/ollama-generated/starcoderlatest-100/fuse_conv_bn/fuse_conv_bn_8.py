
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv = torch.nn.Conv2d(...)  # use convolution layer
        bn = torch.nn.BatchNorm2d(...)  # use batch normalization layer
        
        output = conv(x) 
        output = bn(output)

        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 56, 56)
