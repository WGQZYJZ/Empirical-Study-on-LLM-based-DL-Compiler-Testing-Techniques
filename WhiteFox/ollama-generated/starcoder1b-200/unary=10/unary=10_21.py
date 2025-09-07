
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 20)
 
    def forward(self, x):
        v = self.linear(x)
        return v + 3
 
    def scale(self, x):
        # Apply a scaled ReLU6 activation function to the input tensor
        # e.g. return nn.ReLU()(nn.Sigmoid()(x))
        return torch.clamp_min(v, -128)
 
    def shift(self, x):
        # Apply a shifted ReLU6 activation function to the input tensor
        # e.g. return nn.Tanh()(v + 3)
        return v / 2


# Initializing the model
m = Model()


