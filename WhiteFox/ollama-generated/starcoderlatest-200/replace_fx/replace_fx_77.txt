 2
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = input_tensor.permute(...) # Permute the input tensor
        v2 = torch.nn.functional.linear(v1, ...) # Apply linear transformation to the permuted tensor.
        return v2


# Initializing the model 2
m2 = Model2()


# Inputs to the model 2
x1_2 = torch.randn(1, 2, 2)
__output_2 = m2(x1_2)

