
class Model(torch.nn.Module):
    def __init__(self, split_dim):
        super().__init__()
 
    def forward(self, x1):
        v = torch.split(x1, 2048 * 375, dim=2) # Split the input tensor into several tensors along dimension 2
        return torch.cat([v[i] for i in range(len(v))], split_dim)  # Concatenate these split tensors back together


# Initializing the model
m = Model(split_dim=0)
# Inputs to the model
x1 = torch.randn(3, 256 * 4096 + 512, 128)
__output__  = m(x1)

