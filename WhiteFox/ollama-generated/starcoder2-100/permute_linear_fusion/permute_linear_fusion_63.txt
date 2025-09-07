
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 1)

    def forward(self, x1):
        v1  = x1.permute(0, 2, 1).contiguous() # Permute the input tensor, and then call contiguous to obtain contiguous memory space
        v2  = self.linear(v1)                    # Apply linear transformation directly on the permuted tensor
        return v2

# Initializing the model