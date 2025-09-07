
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 3)
 
    def forward(self, x1): 
        v1 = self.linear(x1)
        v2 = v1 - other_value
        return v2

# Initializing the model
m2 = Model2()


# Inputs to the model
x1 = torch.randn(50, 10)
other_value  = 34683795 # Just pick a random number here (no particular reason to use this one)
