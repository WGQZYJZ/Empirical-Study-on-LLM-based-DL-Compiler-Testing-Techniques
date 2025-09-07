
class Model(torch.nn.Module):
    def __init__(self, dim1, dim2):
        super().__init__()

    def forward(self, x1):
        v1  = torch.mm(x1[0], self.weight)
        v3 = [v1] * len(dim2) # Concatenation of the result tensor along a specified dimension. The number of times is equal to dim_list length in the list.
        return tuple(v3)

# Initializing the model
m  = Model(4, [(5,),(8,)])

