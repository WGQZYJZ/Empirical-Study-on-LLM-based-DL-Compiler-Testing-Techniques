
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3072, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other_tensor # The 'other' tensor is randomly generated and added at line 5 of this model
        return v2


# Initializing the model
m2 = Model()
 
# Inputs to the model
x1  = torch.randn(3, 4) + torch.rand(3, 10).float()
__output__  = m(x1)


