
class Model(torch.nn.Module):
    def __init__(self, 3):
        super().__init__()
        self.conv = torch.nn.ConvXd(in_channels=1, out_channels=2, kernel_size=4)
        self.bn = torch.nn.BatchNormXd(num_features=2, track_running_stats=True)

    def forward(self, x):
        conv = self.conv(x)  # Convolution layer
        bn = self.bn(conv)   # Batch normalization layer (with tracking statistics enabled), and the output of the convolution is used as the input to batch normalization 
        return bn


m = Model(3)
x1  = torch.randn(2, 3, 4, 5)
x2 = x1 + 0.1
__output__  = m(x1)
__output2__ = m(x2)

