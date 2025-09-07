
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        t1, t2 = x1[..., :2], x1[..., 2:]
        v1 = t1.permute(0, 2, 1).contiguous()
        v2 = torch.relu(t2).contiguous()
        return torch.cat([v1, v2], dim=-1)

# Initializing the model
m = Model()

 # Inputs to the model
x1 = ...
