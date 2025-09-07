
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1) # Apply the linear transformation to the input tensor
        return v2

m2 = Model2()


# Inputs to model m
