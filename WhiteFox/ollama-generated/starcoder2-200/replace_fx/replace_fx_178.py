
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, 0.5)
        v2 = torch.rand_like(v1, dtype=torch.float32)

        return (v1, v2)


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 4096)
