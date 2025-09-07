
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 1)

    def forward(self, x1, x2):
        v1 = input_tensor_A.permute(...) # Permute the input tensor A
        v2 = input_tensor_B.permute(...) # Permute the input tensor B
        v3 = torch.bmm(v1, v2) # or torch.matmul(v1, v2)
        return self.linear2(torch.tanh(self.linear1(torch.cat([v3, x2], dim=1))))


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 4, 2)
x2 = torch.randn(1, 2, 2)
