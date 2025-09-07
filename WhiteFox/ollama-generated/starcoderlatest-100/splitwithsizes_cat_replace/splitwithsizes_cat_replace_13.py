
class Model(torch.nn.Module):
    def __init__(self, num_splits=3, cat_dimension=2):
        super().__init__()
 
    def forward(self, x1):
        v  = self.split_tensors(x1, self.num_splits)
        v5  = torch.cat([v[i] for i in range(len(v))], dim) 
        return v6

    @torch.jit.script
    def split_tensors(self, x1, num_splits):
        tensor_0 = x1[:, :8, :, :]
        tensor_1 = x1[:, 8:, :, :]
        tensor_2 = x1
        return [tensor_0, tensor_1, tensor_2]

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
