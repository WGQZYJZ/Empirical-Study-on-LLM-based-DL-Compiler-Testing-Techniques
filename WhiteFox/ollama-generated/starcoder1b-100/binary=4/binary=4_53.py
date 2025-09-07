
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(100, 1)
 
    def forward(self, x1, other):
        return self.linear(x1 + other)


# Initializing the model
m = Model()

# Inputs to the model
input_tensor = torch.randn(1, 100, dtype=torch.float32)
