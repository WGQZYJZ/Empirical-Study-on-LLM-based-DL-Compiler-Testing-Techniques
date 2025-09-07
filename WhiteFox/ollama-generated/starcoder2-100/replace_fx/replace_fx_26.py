
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t2 = torch.nn.functional.dropout(x1, 0.5) # Apply dropout to the input tensor
        return torch.rand_like(t2).sum()


# Initializing the model
m = Model().to('cuda')

# Inputs to the model
inputs = [torch.randn((3, 3), device='cuda')]

# Target output for the model. Please provide it with the corresponding dtype, shape and size according to the input tensor you just provided in `inputs`.
outputs = [torch.ones_like(x1) * 2]
