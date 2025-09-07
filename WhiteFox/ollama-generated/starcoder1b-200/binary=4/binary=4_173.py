
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return other


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 32) # input shape should be (1, input_shape[0], ..., input_shape[d-1])
