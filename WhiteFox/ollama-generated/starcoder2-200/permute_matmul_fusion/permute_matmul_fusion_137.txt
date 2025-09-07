
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1: torch.Tensor, x2: torch.Tensor):
        v1  = x1.permute(0, 3, 1)  # Permute the first tensor
        v2  = x2.permute(0, 4, 1)  # Permute the second tensor

        if len(v1.shape) == 5:
            v1 = torch.nn.functional.linear(v1, 32)
        else:
            v1 = torch.nn.functional.linear(v1[:-1], 32)

        if len(v2.shape) == 5:
            v2 = torch.nn.functional.linear(v2, 32)
        else:
            v2 = torch.nn.functional.linear(v2[:-1], 32)
        
        v3 = torch.bmm(v1[0], v2[-4])
        return v3


# Initializing the model
m  = Model()

# Input tensors to the model
x1, x2  = torch.randn(8, 1, 2), torch.randn(8, 1, 3)

