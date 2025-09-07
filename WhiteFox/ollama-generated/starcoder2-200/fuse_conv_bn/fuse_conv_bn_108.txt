
class Model(torch.nn.Module):
    def __init__(self, conv_channel=256):
        super().__init__()

        self.conv1 = torch.nn.Conv2d(3, conv_channel // 4 * 2, (7, 7))

    def forward(self, input):
        conv = torch.nn.functional.conv2d(input, self.conv1.weight)
        bn = torch.nn.BatchNorm2d(conv.size()[0])
        output = bn(conv)
        return output

m = Model()

 # Initializing the model 
x = torch.randn(4800).reshape(32, 960 // 17, 5 * 17 + 6 - 3)
__output__  = m(x)

# Inputs to the model
x  = torch.randn(1, 3, 28, 28)

