
class Model(torch.nn.Module):
    def __init__(self, conv_out_channel=10):
        super().__init__()
        self.conv  = torch.nn.Conv1d(28*34, conv_out_channel, kernel_size=7) # A convolution layer
        self.bn = torch.nn.BatchNorm1d(num_features=conv_out_channel) # A batch normalization layer

    def forward(self, x):
        return self.bn(self.conv(x))

m  = Model()
