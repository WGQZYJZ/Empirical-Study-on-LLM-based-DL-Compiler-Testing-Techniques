
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 4, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        return torch.tanh(v1)


# Initializing the model
m = Model()


