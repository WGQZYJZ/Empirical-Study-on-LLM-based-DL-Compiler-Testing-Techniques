
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 2)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return torch.tanh(v1)


# Initializing the model
m = Model()

# Inputs to the model
input_tensor = torch.randn(2, 10)
