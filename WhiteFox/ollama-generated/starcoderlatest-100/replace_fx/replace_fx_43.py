
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, 0.5) # Apply dropout to the input tensor
        v2 = torch.rand_like(v1, dtype=torch.int64) # Generate a tensor with the same size as input_tensor filled with random numbers
        return v2


# Initializing the model
m2 = Model2()


# Inputs to the model
x2 = torch.randn(10, 2, 3)
