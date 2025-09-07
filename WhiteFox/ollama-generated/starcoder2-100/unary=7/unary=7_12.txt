
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 128, 512)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = clamp_max(v1 + 3, 6)
        return v2 / 6

# Initializing the model
m = Model()

 # Inputs to the model