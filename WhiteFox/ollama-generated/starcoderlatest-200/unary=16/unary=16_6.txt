
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(3 * 64 * 64, 50)
 
    def forward(self, x1):
        v1 = torch.view(x1, (x1.shape[0], -1))
        v2 = self.fc1(v1)
        v3 = torch.relu(v2)
        return v3

 # Initializing the model
m = Model()
 
 # Inputs to the model
 x1 = torch.randn(1, 3, 64, 64)
 