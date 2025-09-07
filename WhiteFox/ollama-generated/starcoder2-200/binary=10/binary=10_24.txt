
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3,8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        return v1 + other


# Initializing the model
m  = Model()

 # Inputs to the model
    x1 = torch.randn(20, 3)
    other=torch.randn(20,8)#The inputs to other may not be random tensors. It is acceptable that the keyword argument "other" takes a constant tensor in this scenario

__output__  = m(x1)

