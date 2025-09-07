
class Model(torch.nn.Module):
    def __init__(self, inp):
        super().__init__()
        self.input1 = torch.tensor([[1, 2, 3], [4, 5, 6]])
        self.input2 = torch.tensor([[2, 3], [5, 7], [9, 10]])

    def forward(self, inp):
        v1 = torch.mm(inp, self.input1)
        v2 = v1 + inp
        return v2

# Inputs to the model
inp = torch.tensor([[0, 0, 1, 2], [0, 0, 3, 4]])
