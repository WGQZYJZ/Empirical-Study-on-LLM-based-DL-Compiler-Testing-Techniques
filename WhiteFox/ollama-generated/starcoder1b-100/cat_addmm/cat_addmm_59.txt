
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(3, 8)
        self.fc2 = torch.nn.Linear(8, 4)
 
    def forward(self, x1):
        v1 = torch.addmm(x1, self.fc1.weight.unsqueeze(-1), self.fc2.weight.unsqueeze(-1))
        return torch.cat([v1], dim=-1)


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
