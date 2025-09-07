
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.linear_1 = torch.nn.Linear(8 * 64 * 64, 50)
        self.linear_2 = torch.nn.Linear(50, 25)
        self.linear_3 = torch.nn.Linear(25, 10)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.relu(v1)
        v3 = v2.view(v2.size()[0], -1).mm(self.linear_1.weight).mm(self.linear_1.bias)
        v4 = torch.sigmoid(v3).view(-1, 1).to(x1.device)
        v5 = self.linear_2(v4).view(v4.size()[0], -1).mm(self.linear_3.weight).mm(self.linear_3.bias)
        return v5


# Initializing the model
m = Model()

