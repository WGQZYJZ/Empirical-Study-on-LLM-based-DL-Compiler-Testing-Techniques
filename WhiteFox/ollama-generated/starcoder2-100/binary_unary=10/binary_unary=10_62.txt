
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0  = self.linear(x1)
        v2  = v0 + other.value 
        v3  = torch.relu(v2)
        return v3


# Initializing the model
m = Model()
m.