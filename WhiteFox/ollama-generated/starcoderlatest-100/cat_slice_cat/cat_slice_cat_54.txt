
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2, size, index):
        t1 = torch.cat([x1, x2], dim=1)
        t2 = t1[:, 0:size]
        t3 = t2[:, index]
        t4 = torch.cat([t1, t3], dim=1)
        return t4

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 5, 64, 64)
size = 9223372036854775807
index = torch.randint(low=0, high=5, size=(1,))
