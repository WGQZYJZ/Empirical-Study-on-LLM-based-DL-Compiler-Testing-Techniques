
class Model(torch.nn.Module):
    def __init__(self, dim=32):
        super().__init__()
 
        self.linear = torch.nn.Linear(10 * 64, 5)
 
    def forward(self, x1, x2):
        v1  = torch.mm(x1, x2)  # Matrix multiplication of two input tensors

        v2  = torch.cat([v1 for _ in range(dim)])
 
        return v2


# Initializing the model