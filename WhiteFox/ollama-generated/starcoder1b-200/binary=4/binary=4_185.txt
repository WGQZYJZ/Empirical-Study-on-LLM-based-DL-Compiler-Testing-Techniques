
class Model(torch.nn.Module):
    def __init__(self, other=1):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1) + self.other  # Add the output of the linear transformation to the output of the previous layer (the keyword argument "self" refers to the parent module)
        return v1


# Inputs to the model
x1 = torch.randn(3, 2, 64, 64)
