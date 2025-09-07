
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3,8)
 
    def forward(self, x1):
        v1  = self.linear(x1) 
        v2  = v1 - other 
        return v2


# Initializing the model: We will initialize it using an optimizer.
m  = Model()
optimizer = torch.optim.SGD(model.parameters(), lr=0.1, momentum=0.9)
 
# Inputs to the model
x1 = torch.randn(1,3,8)
__output__  = m(x1)

