
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 4) # The first linear transformation
        self.linear2 = torch.nn.Linear(4, 5) # The second linear transformation

    def forward(self, x1):
        v1  = x1.permute(0, 2, 1) # Permute the input tensor A
        v2  = torch.nn.functional.linear(v1, self.linear1.weight, self.linear1.bias) # Apply linear transformation on permuted tensor

        v3  = x1.permute(0, 1, 2) # Permute the input tensor B
        v4  = torch.nn.functional.linear(v3, self.linear2.weight, self.linear2.bias) # Apply linear transformation on permuted tensor

        return self.linear2(self.linear1(x))

# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(4, 5, 3)
__output__  = m(x)