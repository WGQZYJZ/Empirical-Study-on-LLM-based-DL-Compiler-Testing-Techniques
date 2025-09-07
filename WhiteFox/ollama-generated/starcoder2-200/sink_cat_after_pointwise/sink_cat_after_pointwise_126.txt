
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 1)

    def forward(self, x1):
        v0 = x1.permute(0, 2, 1)

        # This is a concatenation pattern.
        # All the tensors that are being concatenated should be of shape (n x 4 x 3).
        v1 = torch.cat([v0, self.linear1.weight], dim=2)
        return v1

# Initializing the model
m  = Model()

 # Inputs to the model: 6 samples with 8x5 elements in each one (784 total elements).
x1 = torch.randn(6, 8, 5)

 # Expected outputs of the model: Concatenated input tensors.
