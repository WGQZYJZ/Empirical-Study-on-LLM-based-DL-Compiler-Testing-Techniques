
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin1 = torch.nn.Linear(50, 784)
        self.lin2 = torch.nn.Linear(784, 64)

    def forward(self, x1):
        v1 = self.lin1(x1)
        v2 = v1 + other_tensor
        v3 = torch.relu(v2)
        return v3

# Initializing the model
m = Model()
other_tensor  = torch.randn(784)

 # Inputs to the model
 x1  = torch.randn(60, 50)
__output__  = m(x1)