
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.cat([x1, x1], dim=0)  # Concatenate the two tensors (a single tensor).
        v2 = v1.view(2, 4)   # Rearrange the concatenated tensor to [tensor1_t1, tensor1_t1, ...] -> [tensor1_t1, tensor2_t1, ..., tensor2_tn]
        v3 = torch.relu(v2)     # Apply a pointwise unary operation (like ReLU or Tanh) to the reshaped tensor.
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 4)
