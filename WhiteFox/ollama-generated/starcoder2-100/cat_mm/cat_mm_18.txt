
class Model(torch.nn.Module):
    def __init__(self, dim = 0) -> None:
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 5)
        self.conv2 = torch.nn.Conv2d(8, 4, 3)
        self.relu = torch.nn.ReLU()
 
    def forward(self):
        v0_1 = self.conv1(x)
        v0_2 = self.relu(v0_1)
        v1_1 = self.conv2(v0_2)
        return torch.cat([v1_1, ..., ...], dim=dim)


m  = Model()
m(input)
