
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 64 * 64, 10)
 
    def forward(self, x):
        v1 = self.linear(x.view(-1, 32*64*64))
        return v1


# Initializing the model
m = Model()

 # Inputs to the model
x  = torch.randn(8, 32 * 64 * 64)
 
# Passing data through the model (adding constant 5.0)
v  = m(x + 5.0)

