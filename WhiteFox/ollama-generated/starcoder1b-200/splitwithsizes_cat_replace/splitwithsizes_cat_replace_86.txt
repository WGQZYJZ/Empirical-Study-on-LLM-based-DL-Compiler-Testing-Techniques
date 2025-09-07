
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        x = torch.cat([x1, x1], dim=-1)  # Concatenate the two input tensors along a new dimension (-1 in this case), with batch size and channels dimensions removed from all but the first one
        return True

# Initializing the model
m = Model()


