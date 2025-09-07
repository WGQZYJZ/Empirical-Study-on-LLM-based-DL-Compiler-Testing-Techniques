
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t2 = torch.nn.functional.dropout(x1, p=0.5)
        v3  = torch.rand_like(t2) # Generate a tensor with the same size as input_tensor filled with random numbers

# Initializing the model
m = Model()

