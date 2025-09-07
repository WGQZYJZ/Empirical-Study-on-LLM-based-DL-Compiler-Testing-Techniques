
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 1)
 
    def forward(self, x):
        v1  = self.linear(x) + self.__other_tensor__
        return v1

# Initializing the model
m  = Model()

 # Other tensor for the new model
other  = torch.randn(32,)
m.__other_tensor__ = other
 
 # Inputs to the model (the same as the previous one)
x1 = torch.randn(64, 32)
__output__  = m(x1)

