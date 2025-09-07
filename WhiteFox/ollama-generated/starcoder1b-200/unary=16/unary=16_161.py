
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 2)
 
    def forward(self, x):
        y = self.linear(x)
        return relu(y)


# Initializing the model
m = Model()


