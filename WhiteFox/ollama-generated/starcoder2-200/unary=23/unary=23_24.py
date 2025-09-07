
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x):
        v  = self.conv(x)
        return torch.tanh(v)

# Initializing the model
m  = Model()


# Inputs to the model