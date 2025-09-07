
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1):
        v1 = torch.cat([x1[:, 0:1], x1[:, 1:]], dim=1) # Concatenate two columns of the input tensor
        v2 = v1.view(-1) # Reshape and flatten the concatenated tensor. The size of the output shape is (n,) where n is the number of elements in the reshaped tensor
        v3 = torch.relu(v2) # Apply a pointwise unary operation to the reshaped tensor
        return self.linear(v3)

# Inputs to the model
x1 = torch.randn(1, 2, 2)
