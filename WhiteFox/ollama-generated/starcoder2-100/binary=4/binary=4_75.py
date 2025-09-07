
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1) 
        v2 = v1 + self.__output__ 
        return v2


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(320, 8 * 64 ** 2)
# The "__output__" is the result of calling the forward method on the previous model
__output__  = m(x1)


