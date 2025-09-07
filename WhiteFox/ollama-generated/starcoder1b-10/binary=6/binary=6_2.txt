
class Model(torch.nn.Module):
    def __init__(self, other=10):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1) - self.other  # The linear transformation 'v' is subtracted from the output of the linear transformation, and then 'other' is added to it
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 10)
