
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, -50)
        v3 = torch.clamp_max(v2, 67890) # Here the maximum value is 67890 and the minimum is -50 as given in the requirements 
        return v3


# Initializing model
m = Model()
x1 = torch.randn(1, 3)

# Generating an output for the above input
