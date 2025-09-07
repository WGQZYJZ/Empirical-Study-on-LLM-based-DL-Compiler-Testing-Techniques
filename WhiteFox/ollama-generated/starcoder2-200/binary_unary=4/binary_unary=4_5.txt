
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self._input = torch.nn.Parameter(
            data=torch.empty((2, 3), dtype=torch.int64))
 
    def forward(self, x1):
        v1  = self._input.clone().detach() + other
        return (v1 - x1).relu_()


# Initializing the model