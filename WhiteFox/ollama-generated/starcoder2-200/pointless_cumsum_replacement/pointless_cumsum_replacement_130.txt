
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self):
        v1 = torch.full([32, 784], 1)
        v2 = convert_element_type(v1, torch.double)
        v3 = torch.cumsum(v2, 1).type(torch.double) # Change the type of elements of tensors and lists to the specified dtype.
        return v3


# Initializing the model