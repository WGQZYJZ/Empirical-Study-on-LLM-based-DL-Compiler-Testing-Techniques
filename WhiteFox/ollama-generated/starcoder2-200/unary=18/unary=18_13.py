class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
       return conv(x1)
 
m = Model()


__input__ = torch.randn(1, 3, 64, 64) # Input tensor to the model (can be randomly generated)
