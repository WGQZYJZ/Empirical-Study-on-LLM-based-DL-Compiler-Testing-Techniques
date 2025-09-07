
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=0)
        self.sig = torch.nn.Sigmoid()
 
    def forward(self, x1):
        x = self.conv_transpose(x1)
        return self.sig(x)


# Initializing the model
m = Model()


