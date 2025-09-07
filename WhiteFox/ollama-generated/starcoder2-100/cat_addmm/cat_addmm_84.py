
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.fc1  = torch.nn.Linear(3 * 64 * 64, 8)
        self.fc2  = torch.nn.Linear(8, 1)

    def forward(self, x1):
        v1  = self.fc1(x1)
        v2  = self.fc2(v1)

        return v2

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(4096, 3 * 64 * 64)
 
 