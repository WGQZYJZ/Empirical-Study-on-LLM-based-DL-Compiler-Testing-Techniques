

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        
        conv  = torch.nn.Conv2d(in_channels=3, out_channels=4, kernel_size=(5, 5), stride=(0, 1))
        batchnorm = nn.BatchNorm2d(num_features=4)
        x2 = torch.nn.functional.conv2d(input=x1, weight=conv.weight, bias=conv.bias,stride=(0, 1))
        return conv(batchnorm(x2))


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, 3, 4) # (batch_size x channel x  height x width)
__output__  = m(x1)

