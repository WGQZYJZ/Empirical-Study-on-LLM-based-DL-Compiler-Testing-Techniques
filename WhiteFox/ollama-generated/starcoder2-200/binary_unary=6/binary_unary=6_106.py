
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256, 10)
 
    def forward(self, x):
        v1  = self.linear(x)
        v2 = v1 - other
        v3 = F.relu(v2)
        return v3


# Initializing the model and setting 'other' to be 98765432109876543210 in 'other' variable.
m  = Model()
other = 98765432109876543210


# Inputs to the model