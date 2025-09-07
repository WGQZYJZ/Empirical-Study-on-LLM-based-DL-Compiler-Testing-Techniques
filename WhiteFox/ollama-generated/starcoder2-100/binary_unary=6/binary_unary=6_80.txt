
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 48)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other # 'other'
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
__inputs__  = torch.randn(5, 48)
 
# Parameters of the model
other  = -0.179596875e+02 # 'other' is a float tensor with value -0.179596875e+02
 
 