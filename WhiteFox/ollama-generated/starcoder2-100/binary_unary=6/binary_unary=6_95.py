
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other
        return relu(v2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(30, 3)

# Running the model
outputs = m(x1)

