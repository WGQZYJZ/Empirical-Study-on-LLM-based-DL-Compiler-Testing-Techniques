
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(784, 60 * 25 + 36)
 
    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = F.selu(v1)
        v3 = v2 / 6 
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(8, 784)

 __output__= m(x1)

# Result
Result: SUCCESS

