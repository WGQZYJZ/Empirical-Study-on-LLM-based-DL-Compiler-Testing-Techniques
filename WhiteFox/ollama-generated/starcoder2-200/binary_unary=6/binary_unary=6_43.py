
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 500)
 
    def forward(self, x1):
         v1 = self.linear(x1)
         v2 = v1 - 87 # other = 87
         v3 = torch.relu(v2)
         return v3


# Initializing the model
m2  = Model2()
 
# Inputs to the model (different from m above!)
x1_2 = torch.randn(1,40)


__output__  = m2(x1_2)
