
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
 
    def forward(self, x):
        # Use the output of `self.linear` as an input to this function:
        return self.linear(x + other)


# Initializing the model
m = Model()


