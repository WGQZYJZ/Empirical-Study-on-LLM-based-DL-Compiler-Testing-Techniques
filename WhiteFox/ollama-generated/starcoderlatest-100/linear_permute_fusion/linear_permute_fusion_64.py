
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)

    def forward(self, x1):
        t1 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)
        v1 = t1.permute(0,2,1)
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 4)
