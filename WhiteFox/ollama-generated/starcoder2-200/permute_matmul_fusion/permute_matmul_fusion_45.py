
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 10)

    def forward(self, x1, x2):
        v1  = x1 .permute(0, 3, 4, 5).contiguous()
        v2  = x2 .permute(0, 2, 3, 6, 7).contiguous().view(-1)

        return torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias), \
                torch.nn.functional.linear(v2, self.linear.weight, self.linear.bias)

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(456789013, 5, 432, 1280, 3) # or 456789013, 432, 1280, 3) # or 1, 3, 432, 1280, 5
x2  = torch.randn(456789013, 10, 432, 1280, 5)
__output__, __output_1__  = m(x1, x2)

