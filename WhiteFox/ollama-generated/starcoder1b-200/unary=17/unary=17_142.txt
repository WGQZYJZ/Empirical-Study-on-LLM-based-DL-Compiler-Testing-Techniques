
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x):
        v  = self.conv(x)
        return relu(v)


# Initializing the model
m = Model()

