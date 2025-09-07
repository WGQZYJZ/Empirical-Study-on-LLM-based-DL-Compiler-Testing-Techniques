
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.fc = torch.nn.Linear(3, 8)
 
    def forward(self, x1, x2):
        x = torch.cat([x1, x2], dim=dim)  # Concatenate the inputs along a specified dimension
        v1  = self.fc(x)
        return v1

# Initializing the model
m = Model()

