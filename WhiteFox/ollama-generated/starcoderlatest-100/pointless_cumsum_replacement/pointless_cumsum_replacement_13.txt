
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.full([x1.shape[0], 1], 1, dtype=x1.dtype, layout=x1.layout, device=x1.device)
        v2 = convert_element_type(v1, x1.dtype)
        v3 = torch.cumsum(v2, 1)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(10, 8, 64, 64) # batch_size x channel x height x width
x2 = torch.randint(0, 9, (1, ), dtype=torch.long).to(device)
