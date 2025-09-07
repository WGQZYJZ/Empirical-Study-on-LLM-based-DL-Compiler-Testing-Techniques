
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.where(v1 > 0., v1, v1 * -self.linear.weight)  # For each element in the boolean tensor, if the element is True, the corresponding element from the output of the linear transformation is chosen, otherwise, the corresponding element from the output of the multiplication by the negative slope is chosen
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
