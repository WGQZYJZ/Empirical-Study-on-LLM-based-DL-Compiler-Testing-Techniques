
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.convT(x1)
        v2 = torch.sigmoid(v1)
        return v2


m = Model()
x1 = torch.randn(32, 800, 800) # Input tensor for the model m with shape [32, 800, 800]
x2 = torch.randn(32, 50, 50) # Input tensor for the model m with shape [32, 50, 50]

