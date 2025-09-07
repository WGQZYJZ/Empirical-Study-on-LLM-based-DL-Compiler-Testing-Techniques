
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
        self.negative_slope = negative_slope

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.where(v1 > 0, v1, -self.negative_slope * (v1 + 1))  # for each element in the output of the linear transformation, if the corresponding element is True, set it to negative_slope * (output+1), otherwise copy the corresponding element from the input of the multiplication by negative slope
        return v2


# Inputs to the model
negative_slope = 0.3  # This will be passed as an argument to forward() and used in the model initialization above.
