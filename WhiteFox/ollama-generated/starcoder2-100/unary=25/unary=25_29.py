
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 3)
 
    def forward(self, x1): 
        v1 = self.linear(x1)
        v2 = (v1 > 0).type_as(v1)  
        v3 = negative_slope * v1
        v4 = torch.where(v2, v1, v3)
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2048, 500).cuda()
negative_slope  = 0.7 # In reality this will be an input value that the user should provide. The point is for you to understand the flow of values through a Leaky ReLU.
__output__  = m(x1)

