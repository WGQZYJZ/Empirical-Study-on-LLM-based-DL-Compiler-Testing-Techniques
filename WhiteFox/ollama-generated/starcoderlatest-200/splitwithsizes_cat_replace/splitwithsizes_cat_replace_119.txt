
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.split(x1, [64, 64], dim=1)
        v2 = torch.cat([v1[i] for i in range(len(v1))])
        return v2


# Model to generate the input tensor (one split tensor should be sufficient for this model since there is no `return True` optimization triggered.)
split_sizes = [64, 64]
concatenated_tensor = torch.cat([torch.rand(1,3, s) for s in split_sizes], dim=0)


# Inputs to the model
x1 = concatenated_tensor  # The input tensor is passed as an input directly since all of its split tensors are used.


