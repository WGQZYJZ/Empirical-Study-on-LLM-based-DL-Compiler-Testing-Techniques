
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.full([x1.shape[0], x2.shape[-2], x2.shape[-3]], 1)
        v2 = convert_element_type(v1, dtype=x2.dtype, layout=x2.layout, device=x2.device, pin_memory=False)
        v3 = torch.cumsum(v2, dim=-1) # Compute the cumulative sum of the elements of the tensor along dimension -1
        return v3


# Inputs to the model
x1 = torch.randn([4, 5]) # Shape: [4, 5]
x2 = torch.randn([10, 1], dtype=torch.bool) # Shape: [10, 1]
