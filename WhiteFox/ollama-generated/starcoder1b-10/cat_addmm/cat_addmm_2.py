
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(4, 1)
 
    def forward(self, x1, x2):
        v1  = self.fc(x1)
        v2  = torch.cat([v1], dim=0)  # Concatenate the result along a specified dimension
        return v2


# Initializing the model
m = Model()


