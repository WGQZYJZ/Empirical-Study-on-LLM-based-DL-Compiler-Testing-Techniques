
class Model(torch.nn.Module):
    def __init__(self, d_in, d_out, n=32):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(d_in, n, 1)
        self.conv2 = torch.nn.Conv2d(n, n, 1)
        self.conv3 = torch.nn.Conv2d(n, d_out, 1)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = self.conv3(v2)
        return v3


# Initializing the model
m = Model(d_in=3, d_out=8, n=32)


