

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.rand_like(x1, dtype=torch.float)  # Generate a tensor with the same size as input_tensor filled with random numbers
        v3 = torch.nn.functional.dropout(v2, p=0.85) # Apply dropout to the generated random tensor
        return x1 * 0.7 + v3

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.rand(4, 4) 

__output__  = m(x1)