
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(10, 8)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = torch.tanh(v1)
        return v2


# Initializing the model and printing its output shape after a forward pass.
m  = Model()

# Inputs to the model:
i0 = torch.randn(5, 10, requires_grad=True)
__output__  = m(i0)

