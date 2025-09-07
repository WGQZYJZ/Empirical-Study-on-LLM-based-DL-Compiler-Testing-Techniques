
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_A = torch.nn.Linear(2, 3)
        self.linear_B = torch.nn.Linear(3, 2)

    def forward(self, x1, x2):
        v1 = input_tensor_A.permute(...)
        v2 = input_tensor_B.permute(...)
        result  = torch.bmm(v1, v2) # or torch.matmul(v1, v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 3, 2)
