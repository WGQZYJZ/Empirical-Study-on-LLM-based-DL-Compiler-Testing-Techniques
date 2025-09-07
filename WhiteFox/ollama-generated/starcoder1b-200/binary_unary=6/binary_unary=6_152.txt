
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4000, 200)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return relu(v1 - 3000)

# Initializing the model
m = Model()

