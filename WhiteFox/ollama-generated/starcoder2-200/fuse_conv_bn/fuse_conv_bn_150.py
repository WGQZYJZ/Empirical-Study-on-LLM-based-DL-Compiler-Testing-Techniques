
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # conv and batch normalization layers will be fused into a single layer for optimization

        conv = torch.nn.Conv2d(3, 40, kernel_size=5)  # X should match with ConvXd
        bn = torch.nn.BatchNorm2d(num_features=40)    # X should match with ConvXd

        output1 = conv(x1)         
        output2 = bn(output1)       # fuse to a single layer, batch normalization will be removed 
        return output2

# Initializing the model