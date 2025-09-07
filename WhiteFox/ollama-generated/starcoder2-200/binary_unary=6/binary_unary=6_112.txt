
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3,8)
 
    def forward(self, x2):
        v1  = self.linear1(x2)
        v2  = v1 - other
        v3  = F.relu(v2)
        return v3


# Initializing the model with `other = torch.randn(3)` as initial value of variable `other` in module `Model`.
m = Model()
m.linear1._parameters['weight'].data = other # initializing the weight of the linear layer as 'other'
__output__  = m(x2)

