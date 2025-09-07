
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(10, 4)
        self.relu   = torch.nn.ReLU()
 
    def forward(self, x1):
        v1 = self.linear(x1) + other
        v2 = self.relu(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
input_tensor  = torch.randn(10, 3, 64, 64)
