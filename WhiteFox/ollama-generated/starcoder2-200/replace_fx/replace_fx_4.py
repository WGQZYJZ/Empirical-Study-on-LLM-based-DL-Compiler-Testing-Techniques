
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout()

    def forward(self, x1):  # Permute the input tensor 
        v2 = torch.rand((3,), device="cpu")
        v1 = torch.nn.functional.linear(x1[:, 0], self.dropout.weight)
        return (v1 * v2).sum()

# Initializing the model
m  = Model()

