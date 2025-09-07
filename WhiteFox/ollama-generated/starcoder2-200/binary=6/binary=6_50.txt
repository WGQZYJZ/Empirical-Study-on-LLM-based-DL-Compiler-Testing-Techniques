
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(512, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other # Replace 'other' in the pattern with some random tensor or scalar
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
x1  = torch.randn(1, 512)
 
 
