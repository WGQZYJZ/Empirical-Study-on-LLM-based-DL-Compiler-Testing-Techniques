
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, size):
        t1 = torch.cat([x1, torch.empty_like(x1)], dim=1)
        t2 = t1[:, 0:9223372036854775807]
        t3 = t2[:, 0:size]
        t4 = torch.cat([t1, t3], dim=1)
        return t4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(5, 8, 64, 64) # 128 MB RAM required for running the model
size = x1.size()[3] - 9
