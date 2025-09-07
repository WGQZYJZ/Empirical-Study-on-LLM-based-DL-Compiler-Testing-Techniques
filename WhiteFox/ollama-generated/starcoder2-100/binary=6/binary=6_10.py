
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(80, 51)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other_tensor
        return v2


# Initializing the model
m2  = Model()
 
 
 # Inputs to the model
other_tensor=torch.randn(640,)
x1  = torch.randn(3, 80)
__output__  = m2(x1)

