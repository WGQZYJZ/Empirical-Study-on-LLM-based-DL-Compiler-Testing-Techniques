
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.bmm(x1, x2) # The main input is x1 and the second tensor is x2. It is similar to scenario 1.
        return torch.matmul(v1, v1) # The second input is an identity matrix and the output should be a diagonal matrix.


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 5, 2)
x2 = torch.randn(3, 3, 5)
