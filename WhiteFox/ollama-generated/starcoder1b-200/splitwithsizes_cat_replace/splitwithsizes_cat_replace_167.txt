
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.split(x1, [2], 1)  # Split along dimension 0 (channels), and store as the two outputs of a `split` operation
        v2 = torch.cat([v1[i] for i in range(len(v1))])  # Concatenate the two outputs of a `split` operation, where `dim=1`.
        return v2


# Initializing the model
m = Model()


