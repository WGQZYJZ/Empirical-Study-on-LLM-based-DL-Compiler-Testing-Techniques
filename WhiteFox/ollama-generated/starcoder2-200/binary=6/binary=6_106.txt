
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1 - other
# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(32, 64) # Assuming that the batch size is 32
other = torch.randn(8).sum()
