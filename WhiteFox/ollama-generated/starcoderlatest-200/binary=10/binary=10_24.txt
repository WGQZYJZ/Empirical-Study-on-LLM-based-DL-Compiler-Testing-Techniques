
class Model(torch.nn.Module):
    def __init__(self, num_inputs: int = 4, num_outputs: int = 2):
        super().__init__()
        self.linear = torch.nn.Linear(num_inputs, num_outputs)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + 0.5
        return v2


# Inputs to the model
x1 = torch.randn(2, 4, 8, 32)
