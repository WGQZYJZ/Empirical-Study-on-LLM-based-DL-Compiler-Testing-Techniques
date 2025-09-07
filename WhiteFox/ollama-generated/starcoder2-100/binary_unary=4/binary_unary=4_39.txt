
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.nn.functional.linear(x1, weight=some_other_tensor) # Applying the linear transformation to an input tensor
        v2  = v1 + some_other_tensor 
        v3  = self._apply_relu(v2) # Calling a function that applies ReLU to another tensor
        return v3

    def _apply_relu(self, v):
            return torch.nn.functional.relu(v)

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(20, 15)


__output__  = m(x1)