
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.cat([x1, x2], dim=1)  # Concatenate tensors along a dimension
        v2 = v1.view(v1.size(0), -1)   # Reshape the concatenated tensor
        v3 = torch.relu(v2)             # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor
        return v3


# Initialization of model, the optimization sink_cat_after_pointwise is not triggered when the input is only one tensor.
m = Model()
__output__  = m(x1)
