

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 32)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other_tensor or constant or 5
        return v2


# Initializing the model and inputs to the model
m = Model()
x1 = torch.randn(4, 10)
other_tensor = torch.tensor([1., 3.]) # This line is an example of using a tensor as 'other'. You may use a different variable name or value for 'other' in your submission


__output__  = m(x1)

