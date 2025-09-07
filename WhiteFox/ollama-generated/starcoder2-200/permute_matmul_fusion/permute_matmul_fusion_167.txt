
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1: torch.Tensor, x2: torch.Tensor):
        v1 = x1.permute([0, 2, 1]) # Permute the input tensor A with 3 dims [0]
        v2 = x2.permute(0, 2) # Permute the input tensor B with 2 dims [0], [2]
        v4 = torch.bmm(v1, v2) # This line of code should be added to the Model forward method.
        return v4


# Initializing the model