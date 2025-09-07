
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(5, 8)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 > 0
        v3 = v1 * -0.07692307843137256 # A negative slope value to simulate the leaky relu function 
        v4 = torch.where(v2, v1, v3) # Where v2 is True choose elements from v1 and where v2 is false choose elements from v3
        return v4


# Initializing the model
m  = Model() 

# Inputs to the model
x1 = torch.randn(80, 5)

# Running the model
