
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v1 = self.convt(x1) 
        v2 = torch.tanh(v1)
        return v2

m = Model()

