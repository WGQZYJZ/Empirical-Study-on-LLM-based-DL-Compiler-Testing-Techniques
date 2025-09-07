
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3,8)
 
    def forward(self, x1):
        v1  = self.linear(x1) + torch.randn_like(v1)
        return v1


# Initializing the model
m2  = Model()


# Inputs to the model (first model)
x1 = torch.randn(1, 3)
__output__  = m(x1)


#Inputs for the second model (different from first one): 
x2 = torch.randn(1, 8)
__output__  = m2(x2)

