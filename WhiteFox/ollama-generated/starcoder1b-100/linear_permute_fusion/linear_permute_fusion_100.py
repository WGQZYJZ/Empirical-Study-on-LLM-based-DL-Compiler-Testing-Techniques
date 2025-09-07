
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(...)

    def forward(self, x1):
        t1  = x1.permute(... , ...)
        v1 = self.linear(t1)
        return v1


# Inputs to the model
x1 = torch.randn(...)
