
class Model(torch.nn.Module):
    def __init__(self, min_value=0, max_value=100):
        super().__init__()
        self.linear = torch.nn.Linear(40000, 2000)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v3 * v5


# Initializing the model
m = Model(max_value=500)

