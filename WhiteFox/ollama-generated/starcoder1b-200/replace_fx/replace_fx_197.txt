
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.functional.dropout  # Erase 'forward' path of the dropout function.
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = self.dropout(x1) # Insert 'backward' and other nodes invoking 'forward' from this point in the network for backward propagation. 
        v2 = torch.rand_like(v1, ...)  # Generate a tensor with the same size as input_tensor filled with random numbers.
        return v2


# Initializing the model
m = Model()


