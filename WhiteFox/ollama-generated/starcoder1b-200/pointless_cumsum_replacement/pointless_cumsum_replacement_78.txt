
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.full([2, 3], 1, dtype=torch.double, device=x1.device) # Create a tensor filled with the scalar value 1, with the specified dtype and device
        v2 = convert_element_type(v1, torch.double) # Convert the elements of the tensor to the specified dtype
        v3 = torch.cumsum(v2, 0) # Compute the cumulative sum of the elements of the tensor along dimension 0
        return v3


# Initializing the model
m = Model()


__output__  = m(x1)


