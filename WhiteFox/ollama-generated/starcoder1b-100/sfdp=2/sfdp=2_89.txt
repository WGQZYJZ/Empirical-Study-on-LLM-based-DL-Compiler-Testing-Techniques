
class Model(torch.nn.Module):
    def __init__(self, scale_factor):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.scale_factor = scale_factor
 
    def forward(self, x1):
        v1 = self.conv(x1)
        qk  = torch.matmul(v1, x1.transpose(-2, -1))
        v4 = self.scale_factor * scaled_qk.softmax(-1)
        return v4


# Initializing the model
m = Model(scale_factor=0.5)

