
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 32 * 8, 10)
 
    def forward(self, x):
        v1 = x + 1 
        return v1


# Initializing the model