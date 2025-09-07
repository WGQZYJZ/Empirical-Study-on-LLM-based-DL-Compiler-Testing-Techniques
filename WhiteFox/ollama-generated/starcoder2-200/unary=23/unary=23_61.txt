
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convt  = torch.nn.ConvTranspose2d(3, 8, kernel_size=1)
 
    def forward(self, x1):
        v1  = self.convt(x1)
        v2  = torch.tanh(v1)
        return v2


# Initializing the model
m  = Model()
 
 # Inputs to the model
 __input__  = torch.randn(10, 3, 64, 64)
 m(__input__)