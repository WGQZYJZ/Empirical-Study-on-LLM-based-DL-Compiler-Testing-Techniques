
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transp = torch.nn.ConvTranspose2d(1, 3, 5, stride=2, padding=2)
 
    def forward(self, x1):
        v1 = self.conv_transp(x1)
        v2 = F.relu(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 1, 32, 32)
