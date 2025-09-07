
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 3, stride=2, padding=1)
 
    def forward(self, x):
        v  = self.conv_transpose(x)
        return torch.sigmoid(v)


# Initializing the model
m = Model()

