
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3072, 1)
 
    def forward(self, x1):
        v1 = linear(x1)
        v2  = relu(v1) 
        return v2

# Initializing the model
m2 = Model2()

# Inputs to the model
x1_2 = torch.randn(3072)

