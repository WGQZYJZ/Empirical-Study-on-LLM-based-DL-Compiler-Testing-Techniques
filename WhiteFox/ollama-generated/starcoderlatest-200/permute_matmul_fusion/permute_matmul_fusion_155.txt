
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_1 = torch.nn.Linear(2, 2)
        self.linear_2 = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = input_tensor_A.permute(...)
        v2 = input_tensor_B.permute(...)
        t3 = torch.bmm(...) # or torch.matmul(...)
        v3 = self.linear_1(v2) * 2 + t3 + self.linear_2(x2)
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
