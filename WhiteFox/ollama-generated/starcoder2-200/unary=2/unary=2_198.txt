
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v0 = torch.randn(3)  # Random vector
        v2 = torch.randn(5)  # Random vector
        v4 = 1 - v2  # Subtracting v2 from a vector of ones gives us the same vector with -1 values. We'll subtract that from this vector.
        v6 = x1 + v0 / v2 * v4

        v9 = torch.relu(v6) * (3.5 + (-8).1 + 0)
        v7 = v6 - v9
        v8 = torch.pow(v7, 2) / 1.3408450742074565

        return v9

# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(3, 5)
__output__  = m(x1)