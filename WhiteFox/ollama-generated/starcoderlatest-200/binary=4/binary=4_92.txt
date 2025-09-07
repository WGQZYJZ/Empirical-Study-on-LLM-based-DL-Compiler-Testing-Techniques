
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 28 * 28, 32)
 
    def forward(self, x1):
        v1 = x1.view(-1, self.linear.in_features)
        v2 = torch.add(v1, self.other)
        return self.linear(v2)


# Initializing the model and specify inputs
m = Model()
m.init_weights()  # Initializes weight values of parameters in m to random normal distribution centered at zero with standard deviation equal to 0.02
x1 = torch.randn(3, 64 * 28 * 28)
