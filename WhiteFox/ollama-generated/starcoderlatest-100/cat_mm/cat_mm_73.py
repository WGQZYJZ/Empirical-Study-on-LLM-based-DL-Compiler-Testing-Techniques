
class Model(torch.nn.Module):
    def __init__(self, num_in1=32, num_out=64):
        super().__init__()
        self.conv = torch.nn.Conv2d(num_in1, num_out, kernel_size=1)
 
    def forward(self, x1):
        v1 = self.conv(x1).squeeze() # the result of conv operation is squeezed to be a single-channel tensor
        v2 = torch.cat([v1] * len(v1))
        return v2


# Initializing the model
m = Model(32, 64)
# Inputs to the model
x1 = torch.randn(1, 32, 64, 64)
