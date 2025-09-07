
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(2048, 16)
        self.fc2 = torch.nn.Linear(16, 512)
 
    def forward(self, x1):
        # ...
        return v6
 
# Initializing the model
m = Model()

 # Inputs to the model
q1 = torch.randn(1, 3072, 128, 48)
k1 = torch.randn(512, 3072, 128, 48)
v1 = torch.randn(512, 3072, 128, 48)
