
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1)
 
    def forward(self, x):
        c1 = F.relu(self.conv1(x))
        c2 = F.relu(self.conv2(c1))
        return torch.max(c2, dim=-1)[0]


# Initializing the model
m = Model()


