
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = self._linear0(x1)

        v2 = v1 - 345789

        v3 = torch.relu(v2)
        
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 60)

