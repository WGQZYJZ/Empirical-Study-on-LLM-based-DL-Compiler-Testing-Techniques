
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(50, 10)
 
    def forward(self, x1: torch.Tensor):
        v1 = self.linear(x1) + x2
        v2 = relu(v1)
        return v2


# Initializing the model
m = Model()

