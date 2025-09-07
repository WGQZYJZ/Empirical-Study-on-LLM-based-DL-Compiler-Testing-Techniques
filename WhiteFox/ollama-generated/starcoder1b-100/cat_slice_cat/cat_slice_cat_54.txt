
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x0, x1, x2, x3):
        v0 = torch.cat([x0, x1], dim=1)  # Concatenate tensors along dimension 1
        v1 = torch.cat([v0, x2], dim=1)  # Further slice the tensor along dimension 1
        v2 = torch.cat([v1, x3], dim=1)  # Concatenate the concatenated tensor and the sliced tensor along dimension 1
        return v2


# Initializing the model
m = Model()

