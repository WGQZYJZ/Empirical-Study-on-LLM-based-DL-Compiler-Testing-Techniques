
class Model(torch.nn.Module):
    def __init__(self, dim=1)
        super().__init__()
        self.conv  = torch.nn.ConvXd(32, 64, (7, 7)) 
        self.bn    = torch.nn.BatchNormXd(dim, eps=0.5, momentum=0.)

    def forward(self, x):
      x1  = self.conv(x) 
      x2  = torch.nn.functional.batch_norm(x1, self.bn.weight, self.bn.bias, training=True)
      return x2

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(3, 64, 56, 56).to('cuda')

 # Fuse ConvXd/BatchNormXd into a single ConvXd layer using 'fuse_conv_bn' optimization
