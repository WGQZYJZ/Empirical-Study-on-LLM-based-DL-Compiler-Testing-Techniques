
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):  # Concatenate 2 tensors along their second dimension and then apply a ReLU to the reshaped result.
        v0 = torch.cat([x1, x2], dim=1)
        v1 = v0.view(-1, v0.shape[1])
        v2 = torch.nn.functional.relu(v1) 
        return v2

# Initializing the model
m  = Model()

# Inputs to the model:
# Shape of tensors are (B, 3).
x1_shape = [5] + 5 * [-1]
x1_value = torch.randn(1)

