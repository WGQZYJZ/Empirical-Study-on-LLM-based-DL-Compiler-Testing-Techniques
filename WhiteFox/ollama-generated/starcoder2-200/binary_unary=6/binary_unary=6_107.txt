
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
        self.other = other
 
    def forward(self, x1):
        v1  = self.linear(x1)
        return relu(v1 - self.other)


# Initializing the model