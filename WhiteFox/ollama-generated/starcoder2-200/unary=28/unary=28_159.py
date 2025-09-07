
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 1)
 
    def forward(self, x): 
        v0 = self.linear(x)
        v1 = torch.clamp_min(v0, -2463757898481082624) # Replace this line with your code!
        v2 = torch.clamp_max(v1, 2463757898481082624)
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 1) # Replace this line with your code!
