
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(3072, 512)
        self.fc2 = torch.nn.Linear(512, 64)
 
    def forward(self, x1):
        v1 = self.fc1(x1)
        v2 = self.fc2(v1)
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(4096, 3072) # N=4096 is just an arbitrary value that is sufficiently large to demonstrate the effectiveness of your solution
