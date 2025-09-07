
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.cat([x1.permute(0, 2, 1), x1.permute(0, 2, 1)], dim=-1)
        v2 = torch.relu(torch.view_as(v1[:, :, :-1], v1).matmul(self.linear.weight))
        return v2


# Initializing the model
m = Model()
x1 = ...
__output = m(x1)


