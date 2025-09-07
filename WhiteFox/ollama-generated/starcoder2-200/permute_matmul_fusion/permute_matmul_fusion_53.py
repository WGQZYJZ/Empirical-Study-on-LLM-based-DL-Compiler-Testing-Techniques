
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v3 = torch.bmm(x1.permute(0, 2, 1), x2) # Permute the input tensors and apply batch matrix multiplication.
        return v3

m  = Model()


x1 = torch.randn(2, 4, 5) # Input tensor A for the model with shape (batch size, dimension_A1, dimension_A2).
x2 = torch.randn(10, 2, 3) # Input tensor B for the model with shape (batch size, dimension_B1, dimension_B2).

