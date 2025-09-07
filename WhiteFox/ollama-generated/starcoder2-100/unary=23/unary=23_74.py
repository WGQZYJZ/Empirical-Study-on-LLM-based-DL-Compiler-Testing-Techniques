
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3,8,1)
 
    def forward(self, x):
        v0 = F.pad(x, [1, 1, 1, 1], 'constant', value=0.) # Pad the input tensor on each side by one row and column
        v1  = self.conv(v0) 
        v2  = torch.tanh(v1)
        return v2

# Initializing the model
m  = Model()

