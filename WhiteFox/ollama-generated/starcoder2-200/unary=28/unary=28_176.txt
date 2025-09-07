
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear = torch.nn.Linear(256, 10)
 
    def forward(self, x1):
        v3 = torch.clamp_max(v2, max_value=1)
        return self.linear(v3)

# Initializing the model
m  = Model()


# Inputs to the model