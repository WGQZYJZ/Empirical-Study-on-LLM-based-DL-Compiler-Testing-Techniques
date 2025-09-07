
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(10,8)
 
    def forward(self, x1):
        v1  = self.linear(x1) 
        v2  = F.relu(v1) 
        return v2


# Initializing the model
m2  = Model2()

# Inputs to the model
x1 = torch.randn(30, 10)
__output__  = m2(x1)

