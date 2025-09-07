
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, **kwargs):
        self.v2  = kwargs["other"]  # The variable named "v3" is passed as a keyword argument in the constructor
        v1  = torch.nn.Linear()(x1)
        v4  = torch.nn.ReLU()((v1 + v2))
        return v4


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(3, 5)
other  = torch.randn(6,) # The variable named "v3" is passed as a keyword argument in the constructor when initializing m.
__output__  = m(x1, other=other)

