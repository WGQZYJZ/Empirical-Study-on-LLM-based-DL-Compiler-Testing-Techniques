
class Model(torch.nn.Module):
    def __init__(self, in_features, out_features, stride=1, padding=0, dilation=1, groups=1,
                 bias=True):
        super().__init__()
        self.conv = torch.nn.Conv2d(in_channels=in_features,
                                    out_channels=out_features,
                                    kernel_size=(1,),
                                    stride=stride,
                                    padding=padding,
                                    dilation=dilation,
                                    groups=groups)

        if bias:
            self.bn = torch.nn.BatchNorm2d(out_features)
        else:
            self.register_parameter('bias', None)

    def forward(self, x):
        conv_input = self.conv(x).permute(0, 3, 1, 2).contiguous() # permute and contiguous to satisfy pattern
        output = F.batch_norm(conv_input,
                               weight=self.bn.weight,
                               bias=self.bn.bias,
                               running_mean=self.bn.running_mean,
                               running_var=self.bn.running_var) # fuse the conv and bn layer into a single bn op
        return output


# Initializing the model
m = Model(2, 3, stride=1, padding=(0,), dilation=(1,))


# Inputs to the model
x = torch.randn(1, 2, 5, 4)
