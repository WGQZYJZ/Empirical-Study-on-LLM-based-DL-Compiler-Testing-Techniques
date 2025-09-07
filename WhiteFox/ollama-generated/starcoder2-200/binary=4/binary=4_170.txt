
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 64)
 
    def forward(self, x1):
        v1 = self.linear(x1) 
        v2 = v1 + self.__other__  # Here the keyword argument "other" is used to indicate that another tensor needs to be added (specified by the keyword argument "__other__") to the output of the linear transformation
        return v2


# Initializing the model with different initial values for the other parameter, and printing out its parameter list.
m = Model()
for name, param in m.named_parameters():
    print(name) # The name "other" will be replaced by the corresponding value when initializing the model
other  = torch.randn(3,64)
