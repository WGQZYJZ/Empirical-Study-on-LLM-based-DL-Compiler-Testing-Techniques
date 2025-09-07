
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v3 = torch.bmm(x1, x2)  # or t3 = torch.matmul(input_tensorA, input_tensorB)
        return v3

# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 2, 2)
x2  = torch.randn(1, 2, 3)

# Initializing a variable to capture the output of the model
