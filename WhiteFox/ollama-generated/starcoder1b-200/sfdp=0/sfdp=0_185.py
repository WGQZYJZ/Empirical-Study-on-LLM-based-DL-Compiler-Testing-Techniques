
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(5, 10)
 
    def forward(self, x1):
        v1 = x1.view(-1, 5)
        return self.linear(v1)


# Initializing the model
m = Model()
x1 = torch.randn(2, 5, requires_grad=True)
y1 = m(x1).sum()
