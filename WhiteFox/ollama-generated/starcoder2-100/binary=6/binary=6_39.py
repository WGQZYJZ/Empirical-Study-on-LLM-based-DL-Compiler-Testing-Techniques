
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 32)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - 584972761 # a random scalar
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(3, 10) # input tensor with 3 rows and 10 columns
__output__  = m(x1)
