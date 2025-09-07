

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v3 = torch.nn.functional.dropout(x1, 0.2) # Apply dropout to the input tensor with dropout probability of 0.2
        v4 = torch.rand_like(v3) # Generate a tensor with the same size as `v3` filled with random numbers. The shape and size of the tensor is determined by `v3`.
        return (v3, v4)

# Initializing the model 
m  = Model()

# Inputs to the model 
x1 = torch.randn(20, 5, 6)


# Outputs from the model 
__outputs__ = m(x1)

# Desired outputs 
 __outputs__ = [
 (torch.zeros_like(x1, dtype=torch.float32), torch.ones((m.training, 1)), torch.ones((m.training, 1))), # Outputs 0 and 1 in the training mode; else -1, 1, 1 
 (torch.zeros_like(x1, dtype=torch.float32), -1., torch.randn_like(v4) #Outputs -1 and a random number in the training mode; else zeros, random numbers, 0
 ]

