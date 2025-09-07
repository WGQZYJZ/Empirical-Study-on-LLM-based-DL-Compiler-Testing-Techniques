
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(input_tensor, ...)
        v2 = torch.rand_like(...)
        return torch.add(v1, v2)

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1000, 2, 2)
