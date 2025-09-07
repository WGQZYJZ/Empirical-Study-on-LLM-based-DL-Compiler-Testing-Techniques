
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 5)
 
    def forward(self, x1):
        v2 = torch.sigmoid(x1)
        return v2


# Initializing the model