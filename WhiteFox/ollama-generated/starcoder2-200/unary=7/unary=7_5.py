
class Model(torch.nn.Module):
    def __init__(self, out_features=2048):
        super().__init__()
        self.linear = torch.nn.Linear(1536, 2048)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 * clamp(min=0, max=6, l1 + 3) / 6
        return v2

# Initializing the model
m = Model()

 # Inputs to the model