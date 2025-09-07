
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1, x2):
        v1 = torch.bmm(x1, x2)
        v2 = torch.matmul(x1, x2)
        return v1 * v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 2, 2) # input_tensor_A
x2 = torch.randn(2, 3, 4) # input_tensor_B
