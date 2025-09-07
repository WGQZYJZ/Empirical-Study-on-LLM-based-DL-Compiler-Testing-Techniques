
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_A = torch.nn.Linear(2, 2)
        self.linear_B = torch.nn.Linear(3, 2)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1) # Permute input tensor A (tensor with more than 2 dimensions)
        v2 = self.linear_A(v1).permute(0, 2, 1)  # Apply linear transformation on permuted input tensor A (tensor with more than 2 dimensions)
        v3 = torch.bmm(v2, x2)  # or torch.matmul(v2, x2)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 3, 2)
