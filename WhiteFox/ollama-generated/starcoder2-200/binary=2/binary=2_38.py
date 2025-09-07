
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other_tensor # <--- 'other' is a tensor or a scalar here
        return v2


# Initializing the model
m  = Model()


# Inputs to the model (tensors with the same shape as the output of the convolution, which is produced by conv)
x1 = torch.randn(1, 3, 64, 64)
