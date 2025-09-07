
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v3  = x1.permute(0, 1, 2) # Swap the middle two dimensions of tensor with 6 elements in total
        v4  = torch.nn.functional.linear(v3, self.linear.weight, self.linear.bias)
        return v4


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(20, 5, 3, 6) # A 4D tensor with 90 elements in total
__output__  = m(x1)

