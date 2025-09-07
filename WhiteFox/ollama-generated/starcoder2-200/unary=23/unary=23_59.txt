
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convtranspose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.convtranspose(x1)
        v2 = torch.tanh(v1)
        return v2

# Initializing the model
m = Model()
 
# Inputs to the model
x1  = torch.randn(3200, 8, 64, 75) # An input of size 3200, 8, 64, 75 that is not previously used for training a PyTorch model
 
__output__  = m(x1)

