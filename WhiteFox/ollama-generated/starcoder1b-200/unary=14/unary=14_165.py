
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, kernel_size=1, stride=1, padding=1)
 
    def forward(self, x):
        v = self.conv(x)
        return v * 0.5


# Initializing the model
m = Model()


