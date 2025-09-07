
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = torch.clamp_min(v1, min_value=-3.94678213) # Setting the minimum value to -3.94678213
        v3 = torch.clamp_max(v2, max_value=0.593345308)  # Setting the maximum value to 0.593345308
        return v3


# Initializing the model
m = Model()

# Input tensor for the model