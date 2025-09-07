
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 3)
        self.linear2 = torch.nn.Linear(3, 2)

    def forward(self, x_A, x_B):
        v1 = x_A.permute(0, 2, 1)
        v2 = x_B.permute(0, 2, 1)
        return torch.bmm(v1, v2).permute(0, 2, 1) + torch.matmul(self.linear1(v1), self.linear2(v2))


# Initializing the model
m = Model()

 # Inputs to the model
x_A = torch.randn(1, 2, 3)
x_B = torch.randn(1, 3, 2)
