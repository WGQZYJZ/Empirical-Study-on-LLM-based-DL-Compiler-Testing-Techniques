
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(3, 8)
 
    def forward(self, x1, x2):
        v1  = self.fc1(x1)
        v2 = torch.cat([v1, x2], dim=1) # Concatenate the result along dimension = 1
        return v2


# Initializing the model
m = Model()

