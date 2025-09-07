
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=-1)  # Concatenate the inputs along dim=2
        v2 = v1.view(-1, 2)          # Reshape to 2D tensor
        v3 = torch.relu(v2)           # Apply ReLU as a pointwise function on this tensor
        return self.linear(v3)       # Perform a linear transformation and apply the output

# Initializing the model
m = Model()


