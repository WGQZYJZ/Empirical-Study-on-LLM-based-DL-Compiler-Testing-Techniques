
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)
        self.other   = other
 
    def forward(self, x1):
        v1 = self.linear(x1) + self.other
        return v1


# Inputs to the model
input_tensor = torch.randn(1, 2)  # The first two inputs are random numbers
__output__  = Model(0)(input_tensor)  # The last input is a linear transformation of the inputs (v1 + other), where "other" is equal to 0

