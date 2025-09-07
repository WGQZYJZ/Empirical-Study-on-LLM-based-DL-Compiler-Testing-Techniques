
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1)
 
    def forward(self, x1, x2):
        t1 = self.conv1(x1)
        t2 = t1 * 0.5
        t3 = t1 * 0.7071067811865476
        t4 = torch.erf(t3)
        t5 = t4 + 1
        t6 = t2 * t5
        return t6


# Initializing the model
m = Model()

