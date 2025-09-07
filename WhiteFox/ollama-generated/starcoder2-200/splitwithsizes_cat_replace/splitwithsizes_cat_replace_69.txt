
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # Input shape: (16, 8, 50)
        t1 = torch.split(x1, [4], dim=2)[-1]
        return torch.cat([t1]*3, dim=-1).shape  # Return a new tensor with the shape of (16, 8, 75), which is the same as concatenating 3 tensors along dimension -1


# Initializing model and inputs to it.
m = Model()

i_s  = torch.randn(16, 4, 50) # Input of shape (16, 8, 50), where the split sizes are [2], the input tensors are x1 and t1
i_t1 = i_s[:,:,:3]
i_t2 = i_s[:,:,3:]


m(torch.cat([x1, x2]))  # The concatenated tensors are not used in the output

