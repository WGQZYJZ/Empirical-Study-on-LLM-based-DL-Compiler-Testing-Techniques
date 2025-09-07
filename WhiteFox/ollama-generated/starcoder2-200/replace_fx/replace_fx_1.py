
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.nn.functional.dropout(x1, 0.8)
        v3 = torch.rand_like(v2, dtype=torch.float64)

# Initializing the model
m = Model()


# Inputs to the model