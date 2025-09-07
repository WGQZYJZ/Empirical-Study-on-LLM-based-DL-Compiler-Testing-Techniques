
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 32)
 
    def forward(self, x1, other):
        v1 = self.linear(x1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 64, dtype=torch.float) # 2 samples
other = torch.randn(1, 32, dtype=torch.float) # 1 sample
