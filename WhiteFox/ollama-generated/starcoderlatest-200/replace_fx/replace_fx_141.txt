 2
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 1)

    def forward(self, x1):
        v1 = torch.rand_like(x1) * (x1 + input_tensor) # Use rand_* functions in the graph
        return v2


# Inputs to the model
x1 = torch.randn(10)
