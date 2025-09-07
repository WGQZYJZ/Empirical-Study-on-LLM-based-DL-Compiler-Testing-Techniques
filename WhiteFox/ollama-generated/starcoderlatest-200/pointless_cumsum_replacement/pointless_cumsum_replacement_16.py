
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.full([100], 1.5, dtype=dtype, layout=layout, device=device, pin_memory=False)
        v2 = convert_element_type(v1, dtype)
        v3 = torch.cumsum(v2, dim=0)
        return (t1 * t2).permute([1, 2, 0]) # Apply transpose to the elements of the tensor returned by permute

# Initializing the model
m = Model()


