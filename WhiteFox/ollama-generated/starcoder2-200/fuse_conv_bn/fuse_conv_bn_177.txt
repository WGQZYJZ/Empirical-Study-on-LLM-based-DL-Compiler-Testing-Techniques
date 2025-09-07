
class MyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self._conv = torch.nn.Conv2d(3, 64, kernel_size=7)
        self._batchnorm1 = torch.nn.BatchNorm2d(num_features=64, affine=True)
        self._batchnorm2 = torch.nn.BatchNorm2d(num_features=980, affine=False)
        self._linear1 = torch.nn.Linear(7 * 7 * 64, num_classes=256)

    def forward(self, x):
        y = self._conv(x) # fuse_conv_bn
        y = self._batchnorm1(y)
        y = self._linear1(y) 
        y = self._batchnorm2(y)
        return y

# Initializing the model
m  = MyModel()

