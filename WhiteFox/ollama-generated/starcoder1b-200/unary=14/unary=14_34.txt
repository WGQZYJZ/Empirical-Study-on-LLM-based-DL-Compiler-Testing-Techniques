
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.t_conv = torch.nn.ConvTranspose2d(8, 4, 1, stride=2, padding=0, output_padding=0)
 
    def forward(self, x):
        v1 = self.t_conv(self.conv(x))
        return sigmoid(v1)


# Initializing the model
m = Model()


