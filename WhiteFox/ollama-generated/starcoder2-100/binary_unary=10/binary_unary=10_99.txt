
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28*28, 10)
 
    def forward(self, x): 
        t1 = self.linear(x.view(-1, 28 * 28))
        return torch.nn.functional.relu(t1 + other)

# Initializing the model and adding the other tensor to it.
other = torch.randn(10)
m  = Model()
__output__  = m(x1, other)

