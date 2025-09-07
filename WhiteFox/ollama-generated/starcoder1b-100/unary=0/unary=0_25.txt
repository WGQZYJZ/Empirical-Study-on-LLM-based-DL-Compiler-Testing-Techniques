
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = F.relu(F.avg_pool2d(self.conv(x1), kernel_size=4))
        v2 = torch.abs(v1)
        v3 = F.pad(v2, [[0, 0], [1, 1], [1, 1], [0, 0]])
        v4 = v2 * v2
        v5 = v3 * v4
        v6 = F.relu(F.elu(self.conv(x1))) + 1
        v7 = torch.log(v6)
        v8 = F.interpolate(v7, scale_factor=0.5, mode='bilinear')
        return v8


# Initializing the model
m = Model()


