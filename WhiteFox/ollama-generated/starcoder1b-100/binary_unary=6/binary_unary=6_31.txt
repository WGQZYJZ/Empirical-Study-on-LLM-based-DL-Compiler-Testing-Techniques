
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)
 
    def forward(self, x1, x2):
        v1  = self.linear(x1) - x2 # 'other' subtracted from the output of the linear transformation
        v2  = torch.relu(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 2, 4, 4) # x1 is 3-dimension
x2 = torch.randn(1, 3, 4, 4) # x2 is 3-dimension
