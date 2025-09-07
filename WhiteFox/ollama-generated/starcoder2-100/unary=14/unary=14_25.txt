
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, kernel_size=1, stride=1)
 
    def forward(self, x):
        v0 = torch.nn.functional.interpolate(x, scale_factor=5., mode='nearest', align_corners=None) 
        v1 = self.conv_transpose(v0)

        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x = torch.randn(3,8,64,64)
