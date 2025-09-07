
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, kernel_size=3, stride=1) # input: [B, Cin, Win, Hin], output: [B, Cin*kernel_size^2, Wout, Hout]
        self.bn = torch.nn.BatchNorm2d(8, affine=True)
    
    def forward(self, x):
        v1 = self.conv1(x) # input: [B, Cin, Win, Hin], output: [B, Cin*kernel_size^2, Wout, Hout]
        v2 = self.bn(v1)   # input: [B, Cin*kernel_size^2, Wout, Hout], output: [B, Cin*kernel_size^2, Wout, Hout]
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 3, 64, 64)
