
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 1)

    def forward(self, x1):
        t1 = torch.cat([x1, ...], dim=0) # Concatenate tensors along a dimension
        t3 = torch.relu(t1)
        return t3


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(2, 2).detach().requires_grad_(True)


__output__  = m(x1).sum()