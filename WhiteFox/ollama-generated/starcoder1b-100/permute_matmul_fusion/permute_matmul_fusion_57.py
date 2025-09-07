
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.bmm(v1, self.linear.weight, self.linear.bias)
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 2, 2)
__output_a = m(x1)  # __output_a is a modified input tensor for x1 before permute
x2  = torch.randn(1, 2, 3, 4)
__output_b = m(x2)  # __output_b is a modified input tensor for x2 before permute

