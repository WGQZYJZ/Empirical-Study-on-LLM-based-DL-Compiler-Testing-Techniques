

class Model(torch.nn.Module):
    def __init__(self, n):
        super().__init__()

    def forward(self, x1, x2):  # This line is added for testing
        v1 = x1.permute(0, 2, 1)  # Permute the input tensor A with index order [0]
        v3 = torch.bmm(v1, x2)    # Apply batch matrix multiplication between v1 and x2

        return v3


# Initializing the model
m = Model()


# Inputs to the model  # This line is added for testing
x1 = torch.randn(1000, 5, 4)
x2 = torch.randn(1000, 4, 8)

