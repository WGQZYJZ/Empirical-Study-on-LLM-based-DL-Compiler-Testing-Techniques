
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 4)
 
    def forward(self, x1): 
        v1 = self.linear(x1) 
        v2 = v1 - other # Replace 'other' with the corresponding value here
        return v2


# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(10, 2)
