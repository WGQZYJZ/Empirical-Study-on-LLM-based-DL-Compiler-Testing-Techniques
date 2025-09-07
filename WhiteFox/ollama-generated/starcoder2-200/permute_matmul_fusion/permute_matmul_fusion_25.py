

class Model(torch.nn.Module):
    def __init__(self, x1, x2):
        super().__init__()
        self.linear = torch.nn.Linear(x1, x2)

    def forward(self, t1):
        return torch.bmm(t1.permute(0, 2, 1), self.linear.weight).permute(0, 2, 1)+ self.linear.bias


# Initializing the model