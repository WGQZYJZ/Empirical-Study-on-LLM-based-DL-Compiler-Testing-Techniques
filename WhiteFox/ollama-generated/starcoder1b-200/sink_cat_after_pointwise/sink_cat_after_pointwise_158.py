
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1):
        v1  = x1.permute(0, 2, 1)
        t1 = v1.reshape(-1, v1.shape[-1])
        t2 = self.linear(t1)
        return t2


# Inputs to the model
x1 = torch.randn(1, 2, 4)
