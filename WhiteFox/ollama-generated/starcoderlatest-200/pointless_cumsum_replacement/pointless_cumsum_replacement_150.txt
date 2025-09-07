
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.input = torch.full([8], 1, dtype=dtype, layout=layout, device=device, pin_memory=False)
 
    def forward(self, x1, x2):
        v1 = torch.cumsum(x2 * 0.5, 1) + 1 # Multiply the elements of the tensor by 0.5, and then add 1 to each element
        return v1
 
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
x2 = torch.randn(1, 32, 64, 64)
