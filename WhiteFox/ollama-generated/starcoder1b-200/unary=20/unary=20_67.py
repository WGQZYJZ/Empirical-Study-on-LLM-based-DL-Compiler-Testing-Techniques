
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 4, stride=2, padding=1)
 
    def forward(self, x):
        return self.conv_transpose(x).view(x.size(0), -1)


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
