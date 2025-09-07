
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1) + other_tensor
        return v1


# Initializing the model
m2 = Model2()

# Inputs to the model
other_tensor  = torch.ones(10) # This tensor will be added as a constant to the output of the linear transformation
x2           = torch.randn(1, 3, 64, 64)
__output__   = m2(x2)


# Validating whether PyTorch successfully passes the new generated model against the previous one with the same set of inputs, and check if there is any difference between the outputs of the two models.

