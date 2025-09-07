
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = x1.permute(0, 3, 2)
        v2  = x2.permute(1, 4, 0).transpose(-1, -2)

        # Use torch.matmul to avoid permute twice
        v3  = torch.matmul(v1, v2)

        return v3


# Initializing the model
m = Model()

# Inputs to the model (for one call of forward())
x1  = torch.randn(10, 5, 4, 6) # Input tensor A: the shape is [B, C1, H_A, W] and is always 2D.
x2  = torch.randn(7, 8, 9, 3) # Input tensor B: the shape is [C2, C3, H_B, W].
__output__  = m(x1, x2)

