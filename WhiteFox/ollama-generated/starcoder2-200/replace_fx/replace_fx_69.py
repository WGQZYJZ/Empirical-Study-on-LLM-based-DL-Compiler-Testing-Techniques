
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2  = torch.rand_like(x1, device='cpu') # Generate a tensor with the same size as input_tensor filled with random numbers
        return (v2 + torch.nn.functional.dropout(x1))


# Initializing the model
m  = Model()
__output__  = m(torch.randn(3,4,5))

