
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
         v1 = self.linear(x1) + self._other
         return v1

# Initializing the model