
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1):
        conv = torch.nn.ConvXd(...)  # ConvXd represents the number of channels in the convolution layer.
        bn = torch.nn.BatchNormXd(...)   # BatchNormXd represents the number of channels in the batch normalization layer.
        conv_output = conv(input)

        return conv_output

m  = Model()


input1  = torch.randn(4, 32, 32, 3) 
