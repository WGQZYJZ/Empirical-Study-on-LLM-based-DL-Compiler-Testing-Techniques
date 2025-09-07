
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 32)
 
    def forward(self, x):
        v = self.linear(x)
        return v


# Inputs to the model
input_tensor = torch.randn(10)
