
class Model(torch.nn.Module):
    def __init__(self, inplace=False):
        super().__init__()
        self.inplace = inplace

    def forward(self, x1):
        t1 = torch.cat([x1[0], x1[2], x1[1]], dim=2)
        t1  = torch.cat([t1[:, :, None, :], t1[:, :, :, None], t1[:, None, ...]], dim=-1) # Concatenate tensors along a dimension, including the last one
        return torch.nn.functional.relu(t1 if self.inplace else t1.permute(0, 2, 3, 1)) # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor


# Initializing the model
m = Model()


