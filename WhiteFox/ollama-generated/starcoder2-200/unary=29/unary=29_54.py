
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(8, 3, 1)

    def forward(self, x1):
         v1  = self.deconv(x1) + 0.5
         return v1

m  = Model()
# Inputs to the model
x1 = torch.randn(1, 7, 64, 64)
