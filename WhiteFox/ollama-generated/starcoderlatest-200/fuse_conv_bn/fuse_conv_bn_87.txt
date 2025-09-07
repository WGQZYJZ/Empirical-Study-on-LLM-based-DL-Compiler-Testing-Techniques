
class Model(torch.nn.Module):
    def __init__(self, channels=1, batch_size=64):
        super().__init__()
        self.conv  = torch.nn.Conv2d(channels, channels, kernel_size=(3,3), stride=(1,1), padding=(0,0), bias=False)
        self.bn    = torch.nn.BatchNorm2d(num_features=channels, eps=1e-5, momentum=0.1, affine=True)
        self.conv2 = torch.nn.Conv2d(channels, channels, kernel_size=(3,3), stride=(1,1), padding=(1,1), bias=False)

    def forward(self, x1):
        # v1 is the input tensor for batch norm layer
        # batch norm uses its running mean and var instead of inputs.
        # The output of conv layer should be used as the input to the batch norm layer
        bn_output = self.bn(self.conv(x1))  # (N, C, H', W') => NCHW or NHWC for channels last format
        x2           = self.conv2(bn_output)   # (N, C, H', W'') => NCHW or NHWC for channels last format

        return x2

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(batch_size, channels=channels, height=height, width=width)
