
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28 * 28, 10)
 
    def forward(self, x):
        v1  = self.linear(x)
        v2  = torch.tanh(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
input_tensor = torch.rand((64))
x = input_tensor * x


