
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 3)
        self.linear2 = torch.nn.Linear(3, 2)

    def forward(self, x1, x2):
        t1 = x1.permute(0, 2, 1)  # Permute the input tensor A
        t2 = x2.permute(0, 2, 1)  # Permute the input tensor B
        v3 = torch.nn.functional.linear(t1, self.linear1.weight, self.linear1.bias)
        v4 = torch.nn.functional.linear(v3, t2, self.linear2.bias)
        return v4

# Inputs to the model
x1  = torch.randn(1, 2, 2)
x2  = torch.randn(1, 3, 2)
