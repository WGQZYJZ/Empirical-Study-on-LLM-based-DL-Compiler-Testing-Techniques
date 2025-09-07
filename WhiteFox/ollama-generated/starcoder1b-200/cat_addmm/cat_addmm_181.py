
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(in_features=40, out_features=8)
        self.fc2 = torch.nn.Linear(in_features=8,  out_features=2)
 
    def forward(self, x1):
        v1 = self.fc1(x1)
        v2 = torch.cat([v1], dim=-1)  # Concatenate the result along axis=-1
        v3 = self.fc2(v2)
        return v3


# Initializing the model
m = Model()


