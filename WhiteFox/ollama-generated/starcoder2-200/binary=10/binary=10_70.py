
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 10)
 
    def forward(self, x1, other):
        v1 = self.linear(x1)
        v2 = v1 + other
        return v2
# Initializing the model
m  = Model()
# Inputs to the model
x1 = torch.randn(3)
other=torch.tensor([[0.,-5,6]]) # some 3*3 matrix to test the previous example
