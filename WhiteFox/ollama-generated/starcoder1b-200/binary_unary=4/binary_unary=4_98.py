
class Linear(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 1)
 
    def forward(self, x):
        v1 = self.linear(x)
        return relu(v1 + other)


# Initializing the model
l = Linear()

