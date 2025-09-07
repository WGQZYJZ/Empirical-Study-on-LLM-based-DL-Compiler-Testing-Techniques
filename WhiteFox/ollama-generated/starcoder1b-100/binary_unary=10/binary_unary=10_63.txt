
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1, y2):
        v1 = self.linear(x1) + y2
        v3 = relu(v1)
        return v3


# Initializing the model
m = Model()


