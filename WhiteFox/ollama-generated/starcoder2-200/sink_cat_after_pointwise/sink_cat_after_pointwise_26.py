
class Model(torch.nn.Module):
    def __init__(self, hidden=4):
        super().__init__()

        self.hidden = hidden
        self.linear1  = torch.nn.Linear(2, 5)

    def forward(self, x1, x2):
        v1  = torch.cat([x1, x2], dim=0) # Concatenate tensors along a dimension
        v2  = v1.view(-1, self.hidden).relu() # Reshape the concatenated tensor to a shape compatible with Linear
        return self.linear1(v2)

# Initializing the model
m = Model()

