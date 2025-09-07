
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1) - 1  # Subtract one from the output of the linear transformation
        return v1


# Initializing the model
m = Model()


