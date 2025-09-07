
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, ...)  # This will not be replaced and thus, the graph will have a reference to it
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(10, 2)
