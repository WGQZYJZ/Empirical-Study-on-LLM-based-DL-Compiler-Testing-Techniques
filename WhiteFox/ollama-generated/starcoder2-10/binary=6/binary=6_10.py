
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(30, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other  # 'other' is a scalar value that may be randomly chosen from the allowed range of values
        return v2


# Initializing model2:
m2  = Model2()


# Inputs to model2: 
x1  = torch.randn(8,30)
__output_m2___  = m2(x1) # this is the output of the model with input x1

# Initializing model