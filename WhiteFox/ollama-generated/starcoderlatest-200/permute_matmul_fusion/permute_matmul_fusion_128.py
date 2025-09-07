
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = input_tensor_A.permute(...)
        v2 = input_tensor_B.permute(...)
        if x2 is None:
            return torch.bmm(v1, v2)
        else:
            return torch.matmul(v1, v2)


# Initializing the model
m = Model()
x2 = torch.randn(1, 4, 2)

# Inputs to the model
x1 = torch.randn(1, 2, 2)
