
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout(p=0.5)

    def forward(self, x1):
        t1  = torch.rand_like(x1, ...)  # Generate a tensor with the same size as input_tensor filled with random numbers
        v2  = torch.nn.functional.dropout(t1, ..., ...)  # Apply dropout to the input tensor.
        return v2
# Initializing the model
m = Model()
