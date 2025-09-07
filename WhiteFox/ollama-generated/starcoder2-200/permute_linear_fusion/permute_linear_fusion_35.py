
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1  = x1.permute(0, 2, 1)
        v2  = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 30, 5)
__output__  = m(x1)

# The input tensor to this model is also generated using a random uniform distribution:

# Initializing the model

