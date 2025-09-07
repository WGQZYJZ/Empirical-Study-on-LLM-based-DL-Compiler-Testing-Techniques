
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)

    def forward(self, x):
        t1 = torch.cat([x, x, x], dim=-1)
        t2 = t1.view(-1, x.shape[-1])
        t3 = torch.relu(t2)
        return self.linear(t3)


# Inputs to the model
