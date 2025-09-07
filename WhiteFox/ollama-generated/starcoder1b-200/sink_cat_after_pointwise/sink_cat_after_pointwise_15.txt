
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1).contiguous()
        v2 = torch.cat([x1, x2], dim=1).view(3)
        return torch.relu(v2 + self.linear(x1))


# Initializing the model
m = Model()


