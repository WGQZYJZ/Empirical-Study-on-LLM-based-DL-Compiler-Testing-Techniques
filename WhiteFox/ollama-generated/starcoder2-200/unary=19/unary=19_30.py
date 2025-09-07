
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256 * 8 * 3 * 3, 10)
 
    def forward(self, x):
        v1 = x.flatten()
        v2 = self.linear(v1)
        return torch.sigmoid(v2)

# Initializing the model
m  = Model()

 # Inputs to the model
x = torch.randn(4096, 8 * 3 * 3)
