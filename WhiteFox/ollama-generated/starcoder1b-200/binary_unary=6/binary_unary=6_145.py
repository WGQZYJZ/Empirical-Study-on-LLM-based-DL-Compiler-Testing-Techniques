
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 16)
 
    def forward(self, x2):
        v1 = self.linear(x2)
        return relu(v1 - 3)


# Initializing the model
m = Model()


