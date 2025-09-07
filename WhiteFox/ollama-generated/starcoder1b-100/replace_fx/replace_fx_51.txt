
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, 0.)  # Generate a tensor with the same size as input_tensor filled with random numbers
        t2 = torch.rand_like(x1)     # Generate a tensor with the same size as input_tensor filled with random numbers
        return t2


# Initializing the model
m = Model()


