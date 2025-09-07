
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256, 10)
 
    def forward(self, x):
        y  = self.linear(x)
        z  = y - other
        return z

# Initializing the model
m = Model()

 # Inputs to the model
    x = torch.randn(4, 32 * 56 * 56),
    y = torch.tensor([[0]] * x.shape[0])
    