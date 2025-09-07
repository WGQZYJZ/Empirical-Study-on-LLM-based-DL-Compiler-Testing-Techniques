
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v  = torch.nn.functional.relu(x)

        conv  = torch.nn.Conv2d(3, 4, kernel_size=5, stride=1)
        bn  = torch.nn.BatchNorm2d(4)
        output  = bn(conv(v)) # the output of convolution is used as input for batch norm
        return v

# Initializing the model
m  = Model()

