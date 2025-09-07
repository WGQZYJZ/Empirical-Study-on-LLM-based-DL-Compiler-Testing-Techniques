
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(32, 16, kernel_size=4)
 
    def forward(self, x):
        return torch.sigmoid(self.conv(x))


# Initializing the model
m = Model()
