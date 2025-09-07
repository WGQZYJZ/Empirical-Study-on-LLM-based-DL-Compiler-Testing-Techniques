
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 10)

    def forward(self, x):
       v1  = torch.nn.functional.dropout(x[0], p=0.3) # Apply dropout with a probability of 0.3 to the first component of input tensor
       v2 = torch.rand_like(v1, dtype=torch.float64)   # Generate a tensor of type float64 with the same size as the first component of the input tensor filled with random numbers
       return self.linear(v2), x[0]

# Initializing the model
m = Model()


# Inputs to the model
inputs  = [torch.randn((1,3)), torch.rand_like(shape=(1, 4))]
outputs  = m(*inputs)

