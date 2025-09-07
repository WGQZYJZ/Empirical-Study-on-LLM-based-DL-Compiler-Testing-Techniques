
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 64 * 1587, 90)
 
    def forward(self, x1): 
        v1 = self.linear(x1)
        return v1 + other


# Initializing the model