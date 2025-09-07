
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t = torch.rand(...)  # Generate a tensor with same size as input_tensor filled with random numbers
        return self.dropout(t)


# Initializing the model
m = Model()

