
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(24, 30)
    
    def forward(self, x1, other=None): 
        v1 = self.linear(x1)
        if not (other is None or other == None or type(other) != str or isinstance(other, torch._six.string_classes)):
            raise ValueError('The `other` argument should be a string')
        else:
            v2  = v1 + other
        return relu(v2)

# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(4, 24)
__output__= m(x1)