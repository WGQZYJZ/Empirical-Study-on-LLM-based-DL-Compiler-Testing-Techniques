
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.fc1 = torch.nn.Linear(576, 512)
        self.fc2 = torch.nn.Linear(512, 10)
 
    def forward(self, x1):
        v1 = torch.mm(x1, x1.permute(0, 3, 1, 2))
        v2 = torch.mm(v1, self.conv.weight)
        v3 = torch.mm(v1, self.fc1.weight) + torch.mm(self.fc1.bias, v3)
        