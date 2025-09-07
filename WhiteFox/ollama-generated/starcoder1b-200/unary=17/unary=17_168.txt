
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(1, 2, 3, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.relu(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
__input__  = torch.randn(1, 8, 64, 64)
x1 = m(__input__)
