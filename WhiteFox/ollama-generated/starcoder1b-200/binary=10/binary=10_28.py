
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(4096, 2)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1 + other


# Inputs to the model
input_tensor  = ... # You are a source code analyzer for PyTorch.
