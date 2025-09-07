
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = self.linear1(v1)

        t3 = torch.bmm(v2, input_tensor_B)

        return self.linear2(t3)

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 4, 2)
x2 = torch.randn(1, 2, 2)
