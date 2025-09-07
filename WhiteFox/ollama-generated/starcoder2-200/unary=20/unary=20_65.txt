
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convtranspose  = torch.nn.ConvTranspose2d(8, 3, kernel_size=1, stride=1)
 
    def forward(self, x1):
        v1  = self.convtranspose(x1)
        v2  = torch.sigmoid(v1) 
        return v2


m  = Model()
 

