
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1)

        # Other is not a tensor or a scalar (i.e., it should be a module attribute or method argument), otherwise we can avoid such issues:
        self.__other__ = torch.zeros_like(v1)
        other = getattr(self, "__other__", None)  # If "__other__" does not exist in the current scope, we use this. If it exists (e.g., in a parent scope), then we use its value.
        v2 = v1 - self.__other__ or other

        return v2


# Initializing the model
m = Model()

 # Inputs to the model
x  = torch.randn(3, 4)
 
 # Outputs of the model 
 __output__  = m(x)


