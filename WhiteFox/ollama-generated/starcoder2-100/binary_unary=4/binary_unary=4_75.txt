
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self._apply(self.__call__, (x1,), {"other": other})
        return v1


# Initializing the model with keyword argument