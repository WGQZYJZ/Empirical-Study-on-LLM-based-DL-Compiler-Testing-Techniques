
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3):
        v1 = torch.cat([x1, x2], dim=0) # Concatenate 3 input tensors along dimension 0
        size  = int(v1.shape[1] / 64 * 64) + 65 
        v2  = v1[:, 0:size] # Slice the concatenated tensor along dimension 1
        return torch.cat([v1, v2], dim=1), x3


# Initializing the model
m = Model()
__output__, __input_tensors__  = m(x1, x2, x3)

# Input tensors to the model (only one of them is allowed; otherwise, please choose randomly.)
x1 = torch.randn([7564, 9]) # Dimension 0: 7564, dimension 1: 9
x2 = torch.randn(73) # Size: 73

