
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 3072)
 
    def forward(self, x1):
        v1 = self.linear(x1) - 512
        v2 = relu(v1)
        return v2


# Initializing the model
m = Model()

