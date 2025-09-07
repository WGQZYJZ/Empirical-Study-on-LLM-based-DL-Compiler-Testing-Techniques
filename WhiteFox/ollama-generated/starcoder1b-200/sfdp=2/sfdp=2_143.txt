
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x, y):
        v = self.conv(x).sum(dim=-2) / (x.shape[-1] * x.shape[-2])
        w = self.conv(y).sum(dim=-1) / (y.shape[-1] * y.shape[-2])
        output = torch.matmul(v, w.transpose(-2, -1))  # Compute the dot product of the two convolution outputs
        return output


# Initializing the model
m = Model()


