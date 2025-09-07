
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x2):
        v2 = self.conv_t(x2)
        return torch.sigmoid(v2)


# Initializing the model
m = Model()


