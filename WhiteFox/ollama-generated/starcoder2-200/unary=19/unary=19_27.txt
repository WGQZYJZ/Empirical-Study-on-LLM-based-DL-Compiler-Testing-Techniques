
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 32 * 8, 10)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = torch.sigmoid(v1)
        return v2

# Initializing the model
m  = Model()

 # Inputs to the model
x = torch.randn(32 * 32 * 8, 10).reshape((1, 32 * 32 * 8))
