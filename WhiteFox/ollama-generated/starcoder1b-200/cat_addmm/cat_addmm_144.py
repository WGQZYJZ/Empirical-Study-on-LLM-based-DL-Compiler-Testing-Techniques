
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(10, 32)
        self.fc2 = torch.nn.Linear(32, 16)
 
    def forward(self, x):
        v1 = torch.cat([x.view(-1, 10), x], dim=-1)  # Concatenate the input tensor along a specified dimension
        v2 = self.fc1(v1)  # Apply Linear to v1 and sum it over the rows of v1
        v3 = self.fc2(v2)  # Apply Linear to v2 and sum it over the columns of v2
        return v3


# Initializing the model
m = Model()

