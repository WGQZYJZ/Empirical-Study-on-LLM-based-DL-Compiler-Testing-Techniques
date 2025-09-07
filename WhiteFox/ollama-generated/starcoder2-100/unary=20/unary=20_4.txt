
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convt  = torch.nn.ConvTranspose2d(3, 8, kernel_size=1)
        self.actfn  = torch.nn.ReLU()
 
    def forward(self, x1):
        v1  = self.convt(x1)
        return self.actfn(v1)


# Initializing the model
m = Model()
 
 # Inputs to the model
x2 = torch.randn(1, 3, 64, 64)
__output_new__  = m(x2)

