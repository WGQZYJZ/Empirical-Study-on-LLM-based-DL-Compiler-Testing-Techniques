
class ConvBnModel(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.conv = torch.nn.Conv2d(1, 32, kernel_size=4)

    def forward(self, input):
        conv = torch.nn.functional.relu(
            self.conv(input)) # X can be 1 or 3 representing the channel dimension
        bn = torch.nn.BatchNorm2d(
            32, momentum=0.9, affine=False) # The affine is set to False
        conv_bn = bn(conv)

        return conv_bn

model = ConvBnModel()


# Input to the model
input1  = torch.randn(4, 16, 57, 32)
__output__  = model(input1)


