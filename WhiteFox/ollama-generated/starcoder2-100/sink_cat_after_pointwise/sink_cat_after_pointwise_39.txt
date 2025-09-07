
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y2):
        v1  = torch.cat([x1[None],y2[:, None]], dim=3) # Concatenate the input tensors along a dimension 
        v2 = v1.view(-1,v1.shape[-1])                  # Reshape the concatenated tensor
        v3 = self._relu(v2)                             # Apply ReLU to the reshaped tensor (the only user of this reshaped tensor)
        return v3

    def _relu(self, x):                                 # Method defined by the user 
        return torch.nn.functional.relu(x)


# Initializing and generating inputs to the model
m = Model()
x1  = torch.randn(2, 2)
y2  = torch.randn(30, 3)
__output__  = m(x1, y2)

