
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.other = torch.randn(4).cuda()
 
    def forward(self, x1):
        v1  = self.conv(x1) + self.other # Note that the input tensor must be on GPU
        v2  = torch.relu(v1)
        return v2


# Initializing the model
m  = Model().cuda()


# Inputs to the model, on GPU:
x1 = torch.randn(4, 3, 80, 96).cuda()
__output__  = m(x1)