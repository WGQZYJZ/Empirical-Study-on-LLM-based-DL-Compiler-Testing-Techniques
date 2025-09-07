
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1)
 
    def forward(self, x1, x2):
        v1 = self.conv1(x1) * 0.5 + self.conv2(x2) * 0.7071067811865476
        v2 = torch.mm(v1, v1) # Apply matrix multiplication between the outputs of conv1 and conv1
        v3 = torch.erf(v2)
        v4 = v3 * 2
        v5 = torch.erf(v4)
        return v5


# Initializing the model
m = Model()

