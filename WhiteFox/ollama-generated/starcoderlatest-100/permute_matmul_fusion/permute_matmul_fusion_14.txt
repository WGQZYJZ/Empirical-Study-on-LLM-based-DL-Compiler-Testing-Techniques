
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1, x2):
        v1 = input_tensor_A.permute(0, 2, 1)
        v2 = input_tensor_B.permute(0, 2, 1)
        t3 = torch.bmm(v1, v2) # or torch.matmul(v1, v2)
        v3 = torch.relu(t3)
        v4 = self.linear(v3)
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
