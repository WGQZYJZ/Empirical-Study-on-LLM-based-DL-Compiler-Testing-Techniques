
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4 * 4 * 8, 2)
 
    def forward(self, x):
        v = torch.cat([x[:, :2], x[:, 2:]], dim=1)
        v = self.linear(v)
        return v


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 4 * 4 * 8, requires_grad=True)
