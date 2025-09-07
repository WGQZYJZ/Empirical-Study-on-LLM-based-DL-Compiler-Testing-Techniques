
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.rand_like(x1)  # Generate a tensor with the same size as input_tensor filled with random numbers
        v1 = torch.nn.functional.dropout(v2, 0.5) 
        return v1


# Initializing the model
m  = Model()

# Inputs to the model