
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.convtranspose  = torch.nn.ConvTranspose2d(32, 8 * 10, kernel_size=4, stride=5)
        self.negative_slope  = negative_slope
 
    def forward(self, x1):
        v1  = self.convtranspose(x1)
        v2  = v1 > 0
        v3  = v1 * self.negative_slope
        v4  = torch.where(v2, v1, v3)
        return v4


# Initializing the model with negative slope of `0.8`
m  = Model(negative_slope=0.8)

 # Inputs to the model
x1  = torch.randn(1, 32 * 5 + 976, 64, 32)
  __output__  = m(x1)

# 