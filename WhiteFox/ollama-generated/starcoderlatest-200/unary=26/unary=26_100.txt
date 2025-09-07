
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(16, 32, 4, stride=2, padding=1)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        negative_slope = torch.tensor(-negative_slope).to(device='cuda', dtype=torch.float32)
        t1 = (v1 > 0).to(dtype=torch.float32)
        t2 = v1 * negative_slope
        v4 = torch.where(t1, v1, t2)
        return v4


# Initializing the model
m = Model()

