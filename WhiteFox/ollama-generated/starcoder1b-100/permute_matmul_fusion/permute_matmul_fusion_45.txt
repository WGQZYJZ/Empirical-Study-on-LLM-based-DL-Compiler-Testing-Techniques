
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_A = torch.nn.Linear(2, 2)
        self.linear_B = torch.nn.Linear(3, 2)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = x2.permute(0, 2, 1)
        t1 = torch.matmul(v1, self.linear_A.weight) # or torch.bmm(t1, self.linear_B.weight)
        t2 = torch.matmul(input_tensor_B, self.linear_A.weight) # or torch.bmm(t1, input_tensor_B)
        v3 = torch.bmm(v1, self.linear_B.weight) # or torch.matmul(t1, self.linear_B.weight)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 2, 2)
x2  = torch.randn(1, 2, 2)
