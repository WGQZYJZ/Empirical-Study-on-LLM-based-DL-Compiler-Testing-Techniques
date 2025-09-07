
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.functional.dropout

    def forward(self, x1):
        v1 = self.dropout(x1, 0.5) # Apply dropout to the input tensor and drop the result with probability 0.5

        return v1


# Initializing the model
m = Model()
__input__ = torch.randn(1, 2, 2) # Generate a random tensor of shape (1, 2, 2)
