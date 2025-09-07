
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(16, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        t1 = self.conv_transpose(x1)
        t2 = torch.tanh(t1)
        return t2


# Inputs to the model
x1 = torch.randn(1, 16, 64, 64)
