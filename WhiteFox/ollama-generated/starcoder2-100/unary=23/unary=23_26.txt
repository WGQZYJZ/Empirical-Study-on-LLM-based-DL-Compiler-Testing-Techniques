
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.conv1 = torch.nn.Conv2d(3, 8, 4)
        self.conv2 = torch.nn.ConvTranspose2d(8, 8, 5)
 
    def forward(self, x1):
        v1  = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = torch.tanh(v2)

        return v3


# Initializing the model