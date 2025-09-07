
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2dTranspose(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x):
        v  = self.conv(x)
        v  = torch.tanh(v)
        return v


# Inputs to the model
x  = torch.randn(1, 8, 64, 64)
