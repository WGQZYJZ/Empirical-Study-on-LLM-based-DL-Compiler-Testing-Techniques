
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)
        v2 = v1.permute(-2, -1).clone() # clone the permuted output tensor so that it doesn't share memory with its previous version
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(3)
__output__  = m(x1).shape

