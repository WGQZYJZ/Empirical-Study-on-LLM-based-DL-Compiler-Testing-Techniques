
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 4)

    def forward(self, x1):
        v1  = torch.cat([x1[:, None], x1[:, None]], dim=0) # Concatenate two input tensors along the first dimension
        v2  = v1.view(-1, 1, 8)                           # Reshape this concatenated tensor to a new shape
        v3  = torch.nn.functional.relu(v2)                # Apply a pointwise unary operation (like ReLU or Tanh) on the reshaped tensor after concatenating two tensors along the first dimension.
        return self.linear(torch.mean(v3, dim=1))

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(4) # Size: [B]
__output__  = m(x1)


