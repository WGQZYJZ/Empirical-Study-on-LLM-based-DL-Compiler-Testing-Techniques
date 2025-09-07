
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.nn.functional.linear(x1, self.weight_A)  # Apply linear transformation to the input tensor A
        v2 = torch.nn.functional.linear(x2, self.weight_B)  # Apply linear transformation to the input tensor B

        t1 = x1.permute(0, 2, 1)  # Permute the input tensor A
        t2 = x2.permute(0, 2, 1)  # Permute the input tensor B

        t3 = torch.bmm(t1, t2)  # or torch.matmul(t1, t2)
        return v1 + v2 + t3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
