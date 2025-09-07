
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = self.conv_block1(x1) * 0.5
        v2 = self.conv_block2(v1) * 0.7071067811865476
        v3 = torch.erf(v2)
        v4 = v3 + 1
        v5 = v2 * v4
        return v5
 
    def conv_block1(self, x):
        self._conv_block1 = None
        if not (self._conv_block1 is not None):
            self._conv_block1 = torch.nn.Sequential(*[
                torch.nn.Conv2d(3, 64, kernel_size=5, stride=1, padding=2),
                torch.nn.BatchNorm2d(64),
                torch.nn.ReLU(inplace=True)
            ])
        return self._conv_block1(x)
 
    def conv_block2(self, x):
        self._conv_block2 = None
        if not (self._conv_block2 is not None):
            self._conv_block2 = torch.nn.Sequential(*[
                torch.nn.Conv2d(64, 80, kernel_size=5, stride=1, padding=2),
                torch.nn.BatchNorm2d(80),
                torch.nn.ReLU(inplace=True)
            ])
        return self._conv_block2(x)
 
 # Initializing the model
m = Model()
 
 # Inputs to the model
 x1 = torch.randn(1, 3, 64, 64)
 