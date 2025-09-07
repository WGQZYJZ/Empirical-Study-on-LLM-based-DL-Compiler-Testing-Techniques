
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.mm(x1, x2) # matrix multiplication of input tensors x1 and x2 
        v2  = torch.cat([v1] * len_list, dim=dim) # concatenate the result tensor along a specified dimension
        return v2

# Initializing the model
m  = Model()

