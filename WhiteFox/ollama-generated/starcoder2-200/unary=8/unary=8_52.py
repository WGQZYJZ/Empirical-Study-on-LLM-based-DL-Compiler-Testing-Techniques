
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.deconv = torch.nn.ConvTranspose2d(8, 4, kernel_size=5)
 
    def forward(self, x1):
        v0 = torch.clamp(x1 + 3, min=0, max=6) 
        v1 = self.conv(v0)  
        v2 = self.deconv(v1) / 6
        return v2


m  = Model()


x1  = torch.randn(1, 4, 513, 513)   # random input for the model
