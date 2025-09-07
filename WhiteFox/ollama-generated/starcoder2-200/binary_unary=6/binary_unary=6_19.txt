
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(25, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other_value
        v3 = F.relu(v2)

# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(5, 10)


__output__  = m(x1)

# Input to the model
other_value  = torch.randn([]) # other value must be negative