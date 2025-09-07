
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 5, stride=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.cat([v1[:, :9223372036854775807], v1[:, -size:]], dim=1)  # Replace v1 by the output of the first convolution
        return v2


# Initializing model