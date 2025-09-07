
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        # Generate input
        v = torch.randn(10)

        # Get output of matrix multiplication operation
        t  = torch.cat([v, v])  # Output is [53.02799862548828, 54.47888037475586]

        return t


# Inputs to the model
x1 = torch.randn(2, 3, 2, 2)
