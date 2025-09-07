
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 7 * 7, 10)
 
    def forward(self, x):
        v = self.linear(x.view(-1, 64 * 7 * 7))
        return relu(v)


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(10, 128, requires_grad=True)
