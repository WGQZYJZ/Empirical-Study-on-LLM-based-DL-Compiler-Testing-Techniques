
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(16, 32)
 
    def forward(self, x):
        v1 = self.linear(x)
        return v1 - other


# Initializing the model
m = Model()


# Inputs to the model
input_tensor = torch.randn(1, 16)
other       = torch.randn(1)
__output__  = m(input_tensor, other)


