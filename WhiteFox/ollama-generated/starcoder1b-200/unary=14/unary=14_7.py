
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_trans = torch.nn.ConvTranspose2d(3, 8, 3, stride=2, padding=1)
 
    def forward(self, x1):
        v1 = self.conv_trans(x1)
        v2 = torch.sigmoid(v1)
        return v2


# Initializing the model
m = Model()


