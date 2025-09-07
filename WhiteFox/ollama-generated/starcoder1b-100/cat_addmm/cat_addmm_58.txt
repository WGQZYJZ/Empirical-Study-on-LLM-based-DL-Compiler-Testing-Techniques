
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(in_features=6, out_features=1)
 
    def forward(self, x1):
        v1 = torch.cat([x1, x1], dim=-1)  # Concatenate the input and itself along a specified dimension
        v2 = torch.addmm(v1, v1, v1)  # Perform a matrix multiplication of itself twice and add it to itself
        return self.fc(v2)


# Initializing the model
m = Model()


