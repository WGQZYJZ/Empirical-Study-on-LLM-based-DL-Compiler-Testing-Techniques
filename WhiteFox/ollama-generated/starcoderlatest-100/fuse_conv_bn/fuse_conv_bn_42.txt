
class Model(torch.nn.Module):
    def __init__(self, dilation=1):
        super().__init__()
        self.conv = torch.nn.ConvXd(..., ...).to_contiguous()
        self.bn  = torch.nn.BatchNormXd(...)

    def forward(self, x):
        if dilation == 1:
            return self.bn(self.conv(x))

        # the convolution layer will be fused with the batch norm layer by default 
        return F.conv2d(x, self.conv, bias=None, stride=(1,1), padding=(0,0), dilation=dilation)

class Model_functional(torch.nn.Module):
    def __init__(self, dilation=1):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)
        self.bn  = torch.nn.BatchNormXd(...).to_contiguous()

    def forward(self, x):
        if dilation == 1:
            return self.bn(F.conv2d(x, self.conv))

        # the convolution layer will be fused with the batch norm layer by default 
        return F.conv2d(x, self.conv, bias=None, stride=(1,1), padding=(0,0), dilation=dilation)
# Initializing the model
m = Model(...).to_contiguous()

# Inputs to the model
x1 = torch.randn(1, 2, ...).to_contiguous()
