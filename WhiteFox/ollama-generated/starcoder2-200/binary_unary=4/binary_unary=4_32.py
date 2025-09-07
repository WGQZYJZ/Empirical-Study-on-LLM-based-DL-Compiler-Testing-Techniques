
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1, other=0):
        v1  = self.conv(x1)
        return v6


# Initializing the model and passing some initial tensor to the forward pass
m  = Model()
x1 = torch.randn(243, 3)

# Calling the forward pass with some input values.
output = m(x1)
output = m(x1, other=torch.tensor(5))

# Saving model to disk using `torch.jit.save`
torch.jit.save(m, 'model_save.pt')