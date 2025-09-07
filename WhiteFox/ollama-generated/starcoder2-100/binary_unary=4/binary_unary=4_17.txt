
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(5, 4)
 
    def forward(self, x1, other=None):
        v2 = None if not hasattr(other, "__getitem__") else len(other) == 1 and other[0].size()
        v3 = (v2,) if v2 is None or type(other).__module__.endswith("ModuleList") else [v2] * x1.size()[1]
        return self.linear(*v3)(x1), other

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(5, 6)

 # Keyword argument for the `other` tensor
kwargs  = { "other": x2 }

# The output of the model is a tuple (v1, v3).
# If the keyword argument `other` was not passed to the model, then only one output will be generated. Otherwise two outputs will be generated, one of which is NoneType and another is an object that contains `x2`.
v1, v2  = m(x1)

