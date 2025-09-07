
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v = torch.cat([x1, x2], dim=1) # Concatenate tensors along the first dimension

        v  = v.view(-1, 60, 30)       # Reshape v
        v  = torch.nn.functional.relu(v)         # Apply ReLU to the reshaped tensor

        return v

m = Model()

