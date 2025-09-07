
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv_transpose  = torch.nn.ConvTranspose2d(3, 8, kernel_size=(7, 5), stride=(4, 3))
 
    def forward(self, x1):
        v1  = self.conv_transpose(x1)
        v2  = (v1 > 0).to(torch.float32) * negative_slope 
        return torch.where(v2 != 0., v1, v2)

# Initializing the model
m  = Model()
negative_slope=0.78539816

# Inputs to the model
x1 = torch.randn(1, 3, 48, 48)
__output__  = m(x1, negative_slope)

