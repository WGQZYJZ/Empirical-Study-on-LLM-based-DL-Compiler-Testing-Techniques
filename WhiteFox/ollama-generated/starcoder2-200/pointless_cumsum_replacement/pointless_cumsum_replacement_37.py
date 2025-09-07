
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x2):
        v1  = torch.full([3072], 1, dtype=torch.float) 
        v4  = convert_element_type(v1, torch.int64) # Convert the elements of the tensor to the specified dtype
        return torch.cumsum(v4, dim=0).view(-1)


# Initializing the model