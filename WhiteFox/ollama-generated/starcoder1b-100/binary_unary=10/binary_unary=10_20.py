
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 10)
 
    def forward(self, x):
        v = self.linear(x)
        return v + other_tensor


# Initializing the model
m = Model()
