
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        t1 = torch.cat([x1[:, :, :], x1[:, :, -2:]], dim=-2)
        t2 = t1.view(-1, 4).permute(0, 2, 1)
        t3 = torch.relu(t2)
        return t3


