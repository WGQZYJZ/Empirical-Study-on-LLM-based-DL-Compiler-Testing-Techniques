
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_A = torch.nn.Linear(2, 2)
        self.linear_B = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1) # Permute the input tensor A
        v2 = torch.nn.functional.linear(v1, self.linear_A.weight, self.linear_A.bias)
        v3 = x2.permute(0, 2, 1) # Permute the input tensor B
        v4 = torch.nn.functional.linear(v3, self.linear_B.weight, self.linear_B.bias)
        result = torch.bmm(v2, v4)
        return result


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 2) # input tensor A (dim > 2)
x2 = torch.randn(1, 2, 2) # input tensor B (dim == 2)
