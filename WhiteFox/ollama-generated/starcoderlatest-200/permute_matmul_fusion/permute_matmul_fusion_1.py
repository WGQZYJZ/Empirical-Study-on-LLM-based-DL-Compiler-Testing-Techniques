
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_A = torch.nn.Linear(2, 2)
        self.linear_B = torch.nn.Linear(2, 3)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1) # Permute the input tensor A to a permuted tensor v1
        v2 = x2.permute(0, 2, 1) # Permute the input tensor B to a permuted tensor v2
        v3 = torch.bmm(v1, v2)  # or torch.matmul(v1, v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
