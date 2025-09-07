
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 2)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other 
        return v2
# Initializing the model
m = Model()


# Inputs to the model
other = torch.randn(2, 5).requires_grad_(True)
x1 = torch.randn(3, 10).requires_grad_()
__output__  = m(x1)

