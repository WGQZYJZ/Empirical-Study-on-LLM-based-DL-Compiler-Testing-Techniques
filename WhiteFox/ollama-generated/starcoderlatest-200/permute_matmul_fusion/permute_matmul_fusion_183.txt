
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.permute(...)  # Permute the input tensor A
        v2 = torch.permute(...)  # Permute the input tensor B
        result_tensor = torch.bmm(v1, v2)
        return result_tensor


# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
