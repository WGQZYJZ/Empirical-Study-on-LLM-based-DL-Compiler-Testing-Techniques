
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, 0.5)  # This dropout node is replaced with a lowmem_dropout node and erased from the graph.
        v2 = torch.rand_like(v1, dtype=torch.float32)  # A random tensor is created here but this tensor will not be erased.
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(10, 8, 4)

