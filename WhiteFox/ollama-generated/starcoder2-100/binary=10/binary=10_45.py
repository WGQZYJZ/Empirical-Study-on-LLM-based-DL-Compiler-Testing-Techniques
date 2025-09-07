
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 20)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other # this is a place holder to specify the tensor that is added to the linear transformation (to be specified during the testing process)
        return v2


# Initializing and using the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(30, 784)

