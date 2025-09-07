
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)
 
    def forward(self, x1):
        return self.linear(x1) + x2  # Add the output of "linear" to the input


# Initializing the model
m = Model()


