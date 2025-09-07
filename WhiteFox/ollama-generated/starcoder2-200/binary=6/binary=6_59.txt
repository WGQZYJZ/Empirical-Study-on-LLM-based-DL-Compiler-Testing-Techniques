
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 - 4  # Assuming 'other' is defined as 4 here in the example
        return v2


# Initializing the model