
class ConvBnModel(torch.nn.Module):
    def __init__(self, channels: int) -> None:
        super().__init__()
        self.conv = torch.nn.Conv2d(3, channels, kernel_size=150)

        self.batchnorm = torch.nn.BatchNorm2d(channels)

    def forward(self, input):
        x  = input.permute(0, 2, 1).contiguous()
        output = torch.nn.functional.conv2d(
            conv=x, weight=self.conv.weight, bias=None if self.conv.bias is None else self.conv.bias)

        return self.batchnorm(output)


model_with_fuse  = ConvBnModel(3)

# Input for the model
input = torch.randn(120, 56)
__output__  = model_with_fuse(input) # This output will be used as input in a further operation.

