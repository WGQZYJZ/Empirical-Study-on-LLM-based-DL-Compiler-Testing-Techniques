
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        negative_slope = -0.2 # Please set a positive number greater than zero to the negative slope in this example
        
        t2 = v1 > 0
        t3 = v1 * negative_slope
        
        t4 = torch.where(t2, v1, t3)
        return t4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
