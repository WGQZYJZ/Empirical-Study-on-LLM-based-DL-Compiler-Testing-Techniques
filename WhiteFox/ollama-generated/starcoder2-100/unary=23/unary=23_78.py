

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, kernel_size=1)
 
    def forward(self, x):
         v1 = self.conv(x)
         return torch.tanh(v1)

# Initializing the model
m = Model()

 # Inputs to the model 
 x  = torch.randn(2048, 3, 64, 64).cuda()
__output__  = m(x)

## End of text
