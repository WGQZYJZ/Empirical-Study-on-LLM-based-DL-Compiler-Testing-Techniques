
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 15)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(32, 20) # Replace 32 with an arbitrarily large number for more than one model example.

# Initializing another tensor 
other  = torch.randn(32, 15)

