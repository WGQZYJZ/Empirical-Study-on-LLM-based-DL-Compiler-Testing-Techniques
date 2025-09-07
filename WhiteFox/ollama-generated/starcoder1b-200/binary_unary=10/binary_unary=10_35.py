
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1) + other
        return relu(v3)


# Initializing the model
m = Model()


