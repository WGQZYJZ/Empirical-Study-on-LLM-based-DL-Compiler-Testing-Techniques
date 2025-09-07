
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other_tensor  # Here 'other_tensor' is some known fixed tensor whose values are not known to the source code analyzers.
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3)
