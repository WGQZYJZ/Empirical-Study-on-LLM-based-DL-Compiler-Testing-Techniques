
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1) - 1  # Subtract 1 from the output of the linear transformation
        v2 = relu(v1)
        return v2


# Initializing the model
m = Model()
