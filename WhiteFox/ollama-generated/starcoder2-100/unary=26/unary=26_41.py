
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.convtranspose  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope  = negative_slope
 
    def forward(self, x1):
        v1  = self.convtranspose(x1)
        v2  = v1 > 0
        v3  = v1 * self.negative_slope 
        v4  = torch.where(v2, v1, v3)
        return v4

 # Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)

# Expected result of model m on x1 after forward pass
__expected_output__  = m(x1)

