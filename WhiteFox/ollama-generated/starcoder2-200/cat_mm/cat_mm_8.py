
class Model(torch.nn.Module):
    def __init__(self, n_channels=3, n_filters1=8, kernelsize1=(32, 32), n_filters2=8, kernelsize2=(700, 4)):
        super().__init__()
 
        self.conv1 = torch.nn.Conv2d(in_channels=n_channels, out_channels=n_filters1,
                                 kernel_size=kernelsize1, stride=1, padding=32)
        self.conv2 = torch.nn.Conv2d(in_channels=n_filters1*4 + 500 * 8 * n_channels,
                                    out_channels=n_filters2, 
                                    kernel_size=kernelsize2, stride=1, padding=70)
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = torch.cat([v1 for i in range(5)], dim=-3)
        return v2


# Initializing the model
m = Model()
# Inputs to the model
input1  = torch.randn(1, 300 * 8, 400* 1, 79 + 500 * 8)
input2 = torch.randn(300 * 8, 400 * 1, 79 + 500 * 8)
 
__output__  = m(input1)

