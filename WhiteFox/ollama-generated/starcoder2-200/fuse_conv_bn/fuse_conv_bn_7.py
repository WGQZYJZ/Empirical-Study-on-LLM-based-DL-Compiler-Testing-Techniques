
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):

        conv = torch.nn.Conv2d(3, 4, kernel_size=5) 
        bn   = torch.nn.BatchNorm2d(num_features=conv.out_channels) 
        output = bn(conv(x))
        return output

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 4096, 2875) # input size

__output___ = m(x1)

