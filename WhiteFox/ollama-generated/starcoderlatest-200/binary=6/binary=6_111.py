
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(16, 32)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - 0.75
        return v2


# Inputs to the model
other = torch.randn(8, 4, 32, 32) # other will be subtracted from v1
