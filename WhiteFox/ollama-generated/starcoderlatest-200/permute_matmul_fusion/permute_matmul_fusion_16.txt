
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(3, 3)

    def forward(self, x1):
        t1 = x1.permute(0, 2, 1) # Permute the input tensor A
        v2 = torch.bmm(t1, self.linear1.weight) # or torch.matmul(t1, self.linear1.weight)

        t2 = v2.permute(0, 2, 1) # Permute the output of `torch.bmm` function on input tensor A
        t3 = torch.nn.functional.linear(t2, self.linear2.weight, self.linear2.bias)

        return t3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 2, 3) # x1 shape [10, 6, 3]
