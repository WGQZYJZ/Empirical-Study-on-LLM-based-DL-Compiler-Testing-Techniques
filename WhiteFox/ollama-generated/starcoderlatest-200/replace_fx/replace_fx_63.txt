
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.nn.functional.dropout(x1, p=0.35) # Apply dropout to the input tensor
        v2 = torch.rand_like(x2)                 # Generate a tensor with the same size as input_tensor filled with random numbers
        return v1 + v2


# Input for the model
x1 = torch.randn(4, 3, 50)
x2 = torch.randn(4, 3, 50)
