
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        x2  = torch.randn(2) 
        v3 = self._cat([x1, x2], dim=0).view(-1)
        v4 = torch.nn.functional.relu(v3)
        return v4

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(2, 5)

 