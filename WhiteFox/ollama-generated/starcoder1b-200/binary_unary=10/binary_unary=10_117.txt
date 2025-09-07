
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3200, 1)
 
    def forward(self, x):
        x_ = self.linear(x) + other
        return relu(x_)


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3200)
