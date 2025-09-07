
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.bmm = torch.nn.Bilinear(2, 3, 4)

    def forward(self, x1, x2):
        v1 = torch.nn.functional.linear(x1, ...).permute(...)  # Permute the tensor A
        v2 = torch.nn.functional.linear(x2, ...).permute(...)  # Permute the tensor B
        v3 = torch.bmm(v1, v2)  # or torch.matmul(v1, v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 4, 2)
x2 = torch.randn(1, 2, 5)
