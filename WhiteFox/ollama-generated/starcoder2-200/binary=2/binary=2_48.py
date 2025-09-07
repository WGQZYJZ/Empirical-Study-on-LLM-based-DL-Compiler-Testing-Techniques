
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other  # 'other' could be a tensor of the same shape as the output of the convolution or a scalar value
        return v2


# Initializing the model
m  = Model()
# Inputs to the model, 'other' is the input data
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

