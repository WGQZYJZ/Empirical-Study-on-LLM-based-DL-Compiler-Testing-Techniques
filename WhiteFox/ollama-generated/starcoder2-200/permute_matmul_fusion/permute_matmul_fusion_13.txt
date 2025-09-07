
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):  # x1 is the first input tensor
        v = torch.permute(x1)  # Permute this first input tensor
        t3 = torch.bmm(v, torch.permute(x2))   # Apply BMM to permuted tensors
        return t3


# Initializing and running the model