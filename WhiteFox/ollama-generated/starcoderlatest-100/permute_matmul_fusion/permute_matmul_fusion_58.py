
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1) # permute input tensor A with the same pattern as described in description of requirements section
        v2 = torch.bmm(v1, x2.permute(0, 2, 1))
        return torch.matmul(self.linear1(v2), self.linear2(x2))


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
