
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.mm(x1, x1)
        v2 = torch.cat([v1] * 8, dim=0) # v2 is 8 tensors with the same shape as x1
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 4) # Tensor with shape (3, 4), which will be flattened to length of `4*8` (= 32) tensor
