
class ConvBnModel(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        
        self.conv = torch.nn.ConvXd(3, 64, kernel_size=7)
        self.bn   = torch.nn.BatchNormXd(dim)
        
    def forward(self, x1):
        v1 = torch.nn.functional.convXd(x1, self.conv) # dim = conv.in_channels (3), out_channels is 64. kernel size is 7, stride = 2
        v2 = torch.nn.functional.batch_norm(v1, self.bn)
# Initializing the model
m = ConvBnModel()

# Inputs to the model
x1 = torch.randn(10, 3, 48, 64) # this is a sample input tensor for your implementation (it will be different from previous ones). It should have a spatial size of 56 x 27 x 4 or larger
__output__  = m(x1)

