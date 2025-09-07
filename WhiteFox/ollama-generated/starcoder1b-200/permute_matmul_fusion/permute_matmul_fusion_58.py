
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_1 = torch.nn.Linear(2, 3)
        self.linear_2 = torch.nn.Linear(3, 4)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.bmm(v1, input_tensor_B.permute(0, 2, 1)) # or torch.matmul(v1, input_tensor_B)
        return torch.relu(self.linear_1(x1) + self.linear_2(x2))


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 4)
x2  = torch.randn(1, 4, 5)
