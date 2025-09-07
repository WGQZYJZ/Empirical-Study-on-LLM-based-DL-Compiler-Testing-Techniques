
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 20)
 
    def forward(self, x):
        return self.linear(x)


# Inputs to the model
x = torch.randn(4, 20, requires_grad=True)
