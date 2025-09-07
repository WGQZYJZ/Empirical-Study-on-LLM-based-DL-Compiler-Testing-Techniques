
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4801936, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear.weight)
        v2 = v1.permute(0, 2, 1)

        return v2

# Initializing the model
m  = Model()
__output__  = m(torch.randn(798534576))

