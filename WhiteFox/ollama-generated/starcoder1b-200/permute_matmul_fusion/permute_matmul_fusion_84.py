
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_A = torch.nn.Linear(2, 2)
        self.linear_B = torch.nn.Linear(3, 2)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.bmm(v1, self.linear_A.weight)  # or torch.matmul(v1, self.linear_A.weight)
        v3 = torch.matmul(self.linear_B.weight, x2)  # or torch.bmm(input_tensor_A, input_tensor_B)
        return v3


# Initializing the model
m = Model()
