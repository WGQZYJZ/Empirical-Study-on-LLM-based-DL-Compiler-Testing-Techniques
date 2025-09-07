
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, ...):
        v = torch.cat([x1, x2], dim=0) # Concatenate x1 and x2 along the first dimension (i.e., channel dimension)
        v = v.view(-1, 16 * 3 * 3) # Reshape concatenated tensor to [-1, 48]
        y = torch.relu(v) 
        return y


# Initializing the model
m = Model()


