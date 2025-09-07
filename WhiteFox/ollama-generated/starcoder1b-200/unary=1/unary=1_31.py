
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 8 * 7, 2)
 
    def forward(self, x1):
        v1 = x1.view(x1.shape[0], -1)  # Flatten the input to two dimensions: Batch size (x1) * Input width (64*8*7).
        v2 = self.linear(v1)  # Apply linear transformation to the output of the previous operation.
        return v2


# Initializing the model
m = Model()


