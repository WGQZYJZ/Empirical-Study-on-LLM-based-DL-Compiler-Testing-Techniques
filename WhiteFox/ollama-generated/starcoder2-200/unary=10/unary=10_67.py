
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(10, 25)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + 3 
        v3  = torch.clamp_min(v2, 0.)
        v4  = torch.clamp_max(v3, 6.)
        return (v4 / 6.).to(torch.int8)


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 10)
__output__  = m(x1)

# Final validation step: check if each output element is between 0 and 6. If not, the output will be incorrect.
assert (m(x1).detach().cpu() <= 6.).all(), 'Output exceeds range.'

