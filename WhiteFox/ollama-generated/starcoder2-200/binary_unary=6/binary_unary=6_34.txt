
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 32)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other # where 'other' is a certain value
        v4 = F.relu(v2)
return v4

