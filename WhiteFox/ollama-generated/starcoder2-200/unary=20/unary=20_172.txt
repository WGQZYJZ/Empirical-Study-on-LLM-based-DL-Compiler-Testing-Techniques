
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convt  = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x):
        v0  = self.convt(x)
        return torch.sigmoid(v0)


# Initializing the model
m  = Model()
 
 # Inputs to the model
x_initial = torch.randn(1, 8, 32, 32)

# The initial output of the model with the input tensor x_initial 
output = m(x_initial)