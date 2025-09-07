
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.5) # Dropout happens before permute and linear functions are applied to the tensor
        v2 = torch.rand_like(v1)                      # Generate a tensor with the same size as v1 filled with random numbers 
        v3 = torch.nn.functional.linear(v2, self.linear.weight, self.linear.bias)
        return v3


# Initializing the model
m2 = Model2()


# Inputs to the model
x2 = torch.randn(1, 2, 2)
__output2__ = m2(x2) # The generated input will be different from previous one because of different dropout probability and random numbers are used during inference.