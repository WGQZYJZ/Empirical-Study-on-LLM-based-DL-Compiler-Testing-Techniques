
class ConvModel(torch.nn.Module):
    def __init__(self, conv, bn):
        super().__init__()
        self.conv  = conv # Convolution layer with XD dimension
        self.bn  = bn

    def forward(self, x1):
        v1  = torch.nn.functional.convXd(x1, self.conv.weight) 
        return self.bn(v1)


# Initializing the model
m  = ConvModel(torch.nn.Conv2d(), torch.nn.BatchNorm3d()) # Initialize with the input ConvXd and BatchNormXd


# Inputs to the model
x1  = torch.randn(1, 4, 8, 6) # Input for the convolution layer of Xd is 4D
__output__  = m(x1) 


# Model