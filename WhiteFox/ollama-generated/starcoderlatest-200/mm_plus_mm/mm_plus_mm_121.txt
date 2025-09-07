
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(64, 32)
        self.fc2 = torch.nn.Linear(32, 16)
 
    def forward(self, x1, x2):
        v1 = self.fc1(x1)
        v2 = F.relu(v1)
        v3 = self.fc2(v2)
        v4 = F.relu(v3)
        __output__  = torch.mm(v4, v4.t())
 
 