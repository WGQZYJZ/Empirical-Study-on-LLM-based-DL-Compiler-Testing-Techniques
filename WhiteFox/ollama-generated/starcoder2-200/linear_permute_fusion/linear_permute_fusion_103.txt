
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)

    def forward(self, x1):
        v2 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias).permute(0, 2, 1) # The permute is applied on the output tensor from a linear function with two input arguments, and the shape of this tensor is (batchsize, 4, 3), which is correct for the scenario.
        return v2

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(10, 5)
__output__  = m(x1)



