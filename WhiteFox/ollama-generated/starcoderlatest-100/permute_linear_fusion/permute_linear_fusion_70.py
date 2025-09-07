
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1) # The permute method is invoked here. The output of the permute function should be a tensor with 3 dimensions, where its second dimension is swapped and then passed as the input to linear.
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias) # The second step of linear transformation will invoke the permute function. Here, the output tensor has three dimensions again.
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
