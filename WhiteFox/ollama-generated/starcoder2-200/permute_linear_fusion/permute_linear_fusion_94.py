
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = input_tensor.permute(0, 3, 4, 5, ...) # The number of dimensions in the permuted tensor. This is larger than 3 because it contains 'input_tensor'
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(4, 5, 6, 7, ...)
__output__  = m(x1)