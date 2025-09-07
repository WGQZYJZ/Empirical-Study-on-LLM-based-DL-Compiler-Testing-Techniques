
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 4)
        self.other   = [5., -0.7]
 
    def forward(self, x1): 
        v1 = self.linear1(x1) # Apply a linear transformation to the input tensor
        return v1 - other


# Initializing the model
m2 = Model2()
__output2__  = m2(torch.randn(1, 3))

