
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 5)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)
        return v1

# Initializing the model
m = Model()


# Inputs to the model
input_tensor  = torch.randn(2,3,5)
output__  = m(input_tensor)
