
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convTranspose = torch.nn.ConvTranspose2d(8, 3, 1)
    
    def forward(self, x1): 
        v1  = convTranspose(x1)
        return torch.tanh(v1)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 8, 32, 32)
