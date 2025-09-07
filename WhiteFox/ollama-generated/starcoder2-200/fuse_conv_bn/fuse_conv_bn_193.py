
class MyConvNd(torch.nn.Module):
    def __init__(self, channels=1024, conv_nd: int = 3):
        super().__init__()

        self.conv_nd = conv_nd
        self.inplanes = 64
        
        self.conv = torch.nn.ConvNd(conv_nd, in_channels * planes, kernel_size)
        self.norm = torch.nn.BatchNormNd(norm_id=norm_id)(self._outch)
        self.relu = torch.nn.ReLU(inplace=True)()
        self.maxpool = torch.nn.MaxPoolNd(conv2d_output_shape)

    def forward(self, x):

        x = conv(x)
        x = norm(x)
        
        return x

m1 = MyConvNd()

input_tensor  = torch.rand(3, 64, 500, 800)
output = m1(input_tensor)

