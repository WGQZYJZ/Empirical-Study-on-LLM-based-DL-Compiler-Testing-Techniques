
class MyModel(torch.nn.Module):
    def __init__(self, convNd=1, batchNormNd=0):
        super().__init__()
        self.conv = torch.nn.ConvNd(2, 3, 3) # X is the convNd 
        self.batchnorm = torch.nn.BatchNormNd(num_features=3*convNd) # X should match with convNd
        self.output = torch.nn.ConvXd() # If convNd != batchNormNd

    def forward(self, x):
        return self.output(self.batchnorm(self.conv(x)))


# Initializing the model
m  = MyModel(1)

# Inputs to the model
__input_to_m__ = torch.randn(3,2*2*2, 50) # The input should match with conv.in_channels * 8

__output__  = m(__input_to_m__)

