
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = F.leaky_relu(self.conv(x1), negative_slope=0.1)
        v2 = F.leaky_relu(v1 * 0.5, negative_slope=0.2)
        v3 = (v1 * v1).pow(1/2)
        v4 = (v3 * v1).pow(1/4)
        v5 = ((v4 / 6).sqrt() + 1.0).to(x1.device)
        v6 = F.leaky_relu((v1 * v5).sqrt(), negative_slope=0.3)
        return F.leaky_relu(v6, negative_slope=0.4)


# Initializing the model
m = Model()


