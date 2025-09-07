
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1) # Permute the input tensor A
        v3 = x2.permute(0, 2, 1) # Permute the input tensor B

        v4 = torch.bmm(v1, v3)   # or torch.matmul(v1, v3)

        v5 = torch.nn.functional.linear(v4, self.linear.weight, self.linear.bias)
        return v5


# Initializing the model