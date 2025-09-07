
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2, ...):
        t1 = torch.cat([x1, x2, ...], dim=0) # Concatenate x1 and x2 along dimension 0 (along the channel dimension).
        t2 = t1.view(...) # Reshape the concatenated tensor
        t3 = torch.relu(t2) # Apply a pointwise unary operation to the reshaped tensor
        return t3


# Initializing the model
m = Model()

