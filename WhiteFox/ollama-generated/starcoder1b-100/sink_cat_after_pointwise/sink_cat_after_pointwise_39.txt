
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(...)

    def forward(self, x1):
        t1  = torch.cat([tensor1, tensor2, ...], dim=...)
        t3 = torch.relu(t2)
        v3 = x1.permute(0, 2, 1)
        return t3 + self.linear(v3)


# Initializing the model
m = Model()


# Inputs to the model
x1 = ...
