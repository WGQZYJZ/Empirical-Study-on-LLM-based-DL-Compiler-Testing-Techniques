
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.bmm(v1, self.linear.weight)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 2)
x2 = torch.randn(1, 4, 2)
__output_a = m(x1)  # Output tensor for input tensor A is permuted and then multiplied by weight matrix
__output_b = m(x2)  # Output tensor for input tensor B is permuted and then multiplied by weight matrix