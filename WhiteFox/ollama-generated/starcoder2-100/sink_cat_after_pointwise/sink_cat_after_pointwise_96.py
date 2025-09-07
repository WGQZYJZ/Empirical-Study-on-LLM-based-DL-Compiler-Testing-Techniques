
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v = torch.cat([x1, x2], dim=0)  # Concatenate two tensors along a given dimension.
        v = v.view(-1)
        v = torch.nn.functional.relu(v)  # Apply ReLU on the concatenated tensor and reshape it back.
        return v

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 200)
x2 = torch.randn(40, 512)
__output__  = m(x1, x2)