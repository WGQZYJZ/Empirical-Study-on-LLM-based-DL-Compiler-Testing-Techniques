
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.cat([x1, self.linear], dim=2)
        v2 = v1.view(-1, 80).transpose(0, 1).contiguous() # Concatenate two input tensors along the second dimension
        v3 = torch.nn.functional.relu(v2)  # Apply ReLU to the reshaped tensor
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 80)

