
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.tensor = None
 
    def forward(self, input_tensor):
        self.tensor  = input_tensor.full([arg1, arg2], 1)  # Create a tensor filled with the scalar value 1, with the specified dtype and layout. The created tensor is pinned to the GPU by default.
        return torch.cumsum(self.tensor, 1)


# Initializing the model
m = Model()

