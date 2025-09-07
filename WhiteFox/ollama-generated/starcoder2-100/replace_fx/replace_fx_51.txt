
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
       t1 = torch.nn.functional.dropout(x1, 0.5) # Apply dropout to the input tensor.
       t2 = torch.rand_like(t1,)  # Generate a random tensor with the same size as the output of previous dropout function.
       return t1 + x1  # Add the dropout tensor and input tensor together to generate output tensors.


# Initializing the model
m = Model()

# Inputs to the model:
x1 = torch.ones(4,3)
__output__  = m(x1)

