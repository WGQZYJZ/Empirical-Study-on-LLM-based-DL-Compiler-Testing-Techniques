
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3, 10)
 
    def forward(self, x1, other=None):
        v1  = self.linear(x1)
        if not (other is None or isinstance(other, torch.Tensor)):
            raise TypeError(f"Keyword argument 'other' must be a Tensor, but was: {type(other)}")
 
        v2  = v1 + other
        v3  = F.relu(v2)
        return v3


# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(1, 3)
 
# Keyword argument is a number and it is passed as a positional keyword argument. 
__output__   = m(x1, other=7.5)

# Keyword argument 'other' must be a Tensor, but was: <class 'float'>
__error__    = m(x1, other="abc")

