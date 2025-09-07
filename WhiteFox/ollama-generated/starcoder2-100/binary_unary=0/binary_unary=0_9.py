
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 + other_tensor
        return v2


# Initializing the model
m  = Model()
__output__  = m(torch.randn(10, 3, 64, 64))


