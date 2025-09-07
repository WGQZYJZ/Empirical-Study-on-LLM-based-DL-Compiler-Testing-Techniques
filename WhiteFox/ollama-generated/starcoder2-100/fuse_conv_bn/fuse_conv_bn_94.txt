
class Model(torch.nn.Module):
    def __init__(self, conv_dim):
        super().__init__()
        self.conv = torch.nn.ConvNd(2, 3, kernel_size=1)
        self.bn   = torch.nn.BatchNormNd(conv_dim)
    
    def forward(self, x):
        conv  = self.conv(x)
        bn    = self.bn(conv)

m0  = Model(3).eval()

__output__  = m0(torch.randn(2, 16))

