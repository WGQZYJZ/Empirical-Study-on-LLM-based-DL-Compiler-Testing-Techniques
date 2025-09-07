
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        t1  = torch.cat([x1[:, :, :size], x1[:, :, size:]], dim=1)
        v1  = self.conv(t1)
        return v1


# Inputs to the model
input_tensor = torch.randn(3, 8, 64, 64)
