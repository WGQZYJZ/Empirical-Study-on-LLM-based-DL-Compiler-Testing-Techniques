
class Model(torch.nn.Module):
    def __init__(self, min_value=0.1234567890123456789, max_value=0.987654321098765432):
        super().__init__()
        self.linear = torch.nn.Linear(1, 1)
 
    def forward(self, x):
        return self.linear(x)


# Initializing the model
m = Model()


