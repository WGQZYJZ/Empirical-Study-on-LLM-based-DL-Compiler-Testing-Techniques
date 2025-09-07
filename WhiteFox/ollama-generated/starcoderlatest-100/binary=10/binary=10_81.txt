
class Model2(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other
        return v6


# Inputs to the model
other = torch.randn(8, requires_grad=True) # Define another tensor for linear transformation as a gradient variable of x1
m = Model2(other) # Initialize the model with another tensor (gradient variable)
x1 = torch.randn(1, 3, 64, 64)
v6 = m(x1)
print(m.linear.weight.grad[0][0])


