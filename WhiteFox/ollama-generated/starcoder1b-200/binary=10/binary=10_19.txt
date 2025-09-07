
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2)
 
    def forward(self, x1, other):
        v1 = self.linear(x1) + other  # Add the two tensors to each other, and then return the output of the linear transformation
        return v1


# Inputs to the model
input_tensor = torch.randn(3, 2)
other       = torch.ones(2, requires_grad=True)
__output__  = Model()(input_tensor, other)

