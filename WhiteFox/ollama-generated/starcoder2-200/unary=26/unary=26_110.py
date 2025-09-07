
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.convtranspose = torch.nn.ConvTranspose2d(3, 8, kernel_size=7, stride=4)
        self.leakyrelu = LeakyReLU(negative_slope=0.5)
 
    def forward(self, x1):
        v1 = self.convtranspose(x1)
        v2 = torch.where((v1 > 0), 1 + (1 / 8369), -(torch.logspace(-7, -3.5, 433)[-5:]).reshape(-1, 1))
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
