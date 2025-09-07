
class Model(torch.nn.Module):
    def __init__(self, c1, c2):
        super().__init__()
        self.linear = torch.nn.Linear(c1 + c2, 3)

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=0).view(-1, x1.size(-1)) 
        return torch.relu(t1 @ self.linear(torch.ones(len(t1), 3)))


# Initializing the model