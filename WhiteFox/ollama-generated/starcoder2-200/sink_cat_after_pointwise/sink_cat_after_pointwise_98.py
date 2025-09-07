
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=0) # Concatenate tensors along a dimension 
        v2 = v1.view(-1, 2, 3)  # Reshape the concatenated tensor
        return torch.nn.functional.relu(v2).sum()

m = Model()

