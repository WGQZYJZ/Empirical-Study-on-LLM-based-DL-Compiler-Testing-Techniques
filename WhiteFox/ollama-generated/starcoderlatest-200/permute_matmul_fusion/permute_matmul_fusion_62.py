
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1) # Permute the input tensor A
        v2 = torch.bmm(v1, x2) # or torch.matmul(v1, x2)

        v3 = x2.permute(0, 2, 1) # Permute the input tensor B
        v4 = torch.bmm(x1, v3) # or torch.matmul(x1, v3)

        return (v1 + v2).unsqueeze(-1) + (v3 + v4).unsqueeze(-2)

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
