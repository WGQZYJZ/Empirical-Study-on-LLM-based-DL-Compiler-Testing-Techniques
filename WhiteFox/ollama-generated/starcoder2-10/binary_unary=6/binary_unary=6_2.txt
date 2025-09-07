
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 18)

    def forward(self, x1):
      v1 = self.linear(x1)
      v2 = v1 - other
      v3 = nn.functional.relu(v2)
      return v3

# Initializing the model
m = Model()
other = torch.zeros(18).cuda() # Replace 'other' with a constant value of 0s in the output

# Inputs to the model
x1 = torch.randn(1, 18).cuda()
__output__  = m(x1)

