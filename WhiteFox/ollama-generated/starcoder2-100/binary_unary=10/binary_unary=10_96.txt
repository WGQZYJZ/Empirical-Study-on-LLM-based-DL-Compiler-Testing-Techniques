

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.nn.Linear()(x1)
        v2  = self._add(v1) 
        v3  = self.__relu(v2)
        return v3

# Initializing the model
m  = Model()

