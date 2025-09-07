
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 40)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 * clamp(min=0, max=6, l1 + 3) # clamp is the custom operator
        v3 = v2 / 6 # divide is the custom operator
        return v3

# Initializing the model
m = Model()


# Inputs to the model