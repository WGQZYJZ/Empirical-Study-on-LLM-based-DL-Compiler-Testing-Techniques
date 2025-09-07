
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 4, stride=2, padding=0, output_padding=(1, 0))
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = self.conv_transpose(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 3, 64, 64)
