
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=1) # Concatenate the input tensors along a dimension (axis=1). The resulting tensor should be rank=3.
        t2 = t1.view(-1, 2) # Reshape the concatenated tensor with a new first dimension. The resulting tensor should be rank=4
        t3 = torch.relu(t2) # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor with new dimensions added at the beginning.
        return self.linear(t3)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 2, 2) # Tensor containing [0, 0], shape=torch.Size([2, 2, 2])
x2 = torch.randn(3, 4, 5) # Tensor containing [0, 0], shape=torch.Size([3, 4, 5])
