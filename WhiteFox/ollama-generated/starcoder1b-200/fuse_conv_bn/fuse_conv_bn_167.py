
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...) # X can be 1, 2, or 3 representing the dimension
        self.bn  = torch.nn.BatchNorm2d(...) # X should match with ConvXd

    @torch.jit._export("forward", output_type=(int32,))
    def forward(self, x):
        conv = self.conv(x)
        bn = self.bn(conv)
        return bn


# Inputs to the model
x  = torch.randn(1, 2, 2)
