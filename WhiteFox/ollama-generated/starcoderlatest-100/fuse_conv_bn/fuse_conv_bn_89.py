
class Model(torch.nn.Module):
    def __init__(self, conv_type='conv1d'):
        super().__init__()
        self.bn = torch.nn.BatchNormXd(...)

    def forward(self, x):
        conv  = torch.nn.ConvXd(...)
        if conv_type == 'conv2d':
            output = conv(x) 
        elif conv_type == 'conv3d':
            output = conv(x, stride=1, padding=0, dilation=1, groups=1, bias=True)
        else:
            output = self.bn(conv(x))  # batch normalization layer fused into convolution layer
        
        return output


# Initializing the model with the specified `conv_type`
m  = Model('conv3d')


# Inputs to the model
x1 = torch.randn(1, 2, 4, 4)
