
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 3)
        self.linear2 = torch.nn.Linear(3, 4)

    def forward(self, x1, x2):
        v1 = input_tensor_A.permute(...) # Permute the input tensor A
        v2 = input_tensor_B.permute(...) # Permute the input tensor B
        v3 = torch.bmm(...) # or torch.matmul(...)
        return self.linear1(torch.cat([v1, v2], dim=-1)) + self.linear2(v3)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 3, 3)
