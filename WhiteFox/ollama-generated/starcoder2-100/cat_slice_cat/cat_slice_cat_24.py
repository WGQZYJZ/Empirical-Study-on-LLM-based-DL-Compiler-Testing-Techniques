
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, *args):
        v1 = torch.cat(*args, dim=1)
        v2 = v1[:, 0:9223372036854775807]
        return v2


# Initializing the model
m = Model()


# Inputs to the model
a1 = torch.randn(batch_size, size) # Concatenated tensors from a list of PyTorch tensors.
__output__  = m(*a1)  # Slice the input tensors from an initial concatenation along dimension 1


