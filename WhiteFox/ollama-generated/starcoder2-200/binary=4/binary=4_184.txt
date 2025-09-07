
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(784, 50)
 
    def forward(self, x1):
        v1 = self.linear1(x1) + x2 
        return v1

# Initializing the model
m  = Model()

