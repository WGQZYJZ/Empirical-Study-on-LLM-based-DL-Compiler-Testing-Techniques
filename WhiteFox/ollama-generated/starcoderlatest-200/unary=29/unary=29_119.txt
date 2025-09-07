
class Model(torch.nn.Module):
    def __init__(self, min_value=0.0, max_value=1.0):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, kernel_size=4, stride=4)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp_min(v1, min_value=0.0)
        v3 = torch.clamp_max(v2, max_value=1.0)
        return v3


# Initializing the model
m = Model()
print('Min value: ' + str(m.conv_transpose.min))
print('Max value: ' + str(m.conv_transpose.max))

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
