
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Parameter(torch.randn(256, 100), requires_grad=True) # A random initialization of the query tensor for the model
        self.key = torch.nn.Parameter(torch.randn(100, 4096), requires_grad=True) # A random initialization of the key tensor for the model
        self.value = torch.nn.Parameter(torch.randn(256, 4096), requires_grad=True) # A random initialization of the value tensor for the model
 
    def forward(self, x1):
        v1 = torch.matmul(x1, self.query)  # Compute the dot product of the input and the query tensors
        v2 = v1.div(math.sqrt(torch.pow(v1.norm(p=2, dim=-1), 0.5) + 1e-8)) # Scale the dot product by the inverse of the square root of the sum of absolute values of the inputs and then apply the softmax function
        v3 = torch.nn.functional.dropout(v2, p=self.p) # Apply dropout to the softmax output
        return torch.matmul(v3, self.value)


# Inputs to the model
x1  = torch.randn(4, 64, 64)
__output__  = Model()(x1)

