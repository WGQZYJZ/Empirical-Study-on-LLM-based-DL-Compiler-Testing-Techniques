
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 128)
 
    def forward(self, x1, other=None):
        v1  = self.linear(x1)
        if not other is None:
            v2  = v1 + other

        return relu(v2), v3


# Initializing the model