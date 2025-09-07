
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x0, x2):
        v0 = torch.cat([x0, x2], dim=3) # Concatenate the input tensors along dimension 1
        v1 = v0[:, :, 0:64]              # Slice the concatenated tensor along dimension 1
        return v1


# Initializing the model
m  = Model()
