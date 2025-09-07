
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32768, 50)
 
    def forward(self, x1):
        v1 = self.linear(x1) + 1 # Add a constant to the output of the linear transformation
        return relu(v1)


# Initializing the model
m = Model()


