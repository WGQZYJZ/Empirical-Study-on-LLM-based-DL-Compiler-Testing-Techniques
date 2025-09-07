
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.linear  = torch.nn.Linear(1024*384*576*96, 1)
        self._other  = other
 
    def forward(self, x):
        v1  = self.linear(x) + self._other # Add another tensor to the output of the linear transformation
        v2  = torch.nn.functional.relu(v1) 
        return v2


# Initializing the model