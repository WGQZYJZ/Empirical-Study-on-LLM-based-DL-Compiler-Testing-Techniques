
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.split_with_sizes = torch.split(x1, 40)  # Split x1 into tensors of size 40 along the first dimension

    def forward(self, input_tensor):
        concatenated_tensors = torch.cat([self.split_with_sizes[i] for i in range(len(self.split_with_sizes))], dim=1) # Concatenate split tensors along the first dimension
        return concatenated_tensors


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(80, 3, 64, 64)

# Output of the model with the inputs x1
__output__  = m(x1)

