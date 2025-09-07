
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2048, 196)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v3 = relu(v1 + other)
        return v3


# Initializing the model