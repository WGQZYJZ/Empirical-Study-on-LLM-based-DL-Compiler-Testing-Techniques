class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v0 = torch.matmul(x1, x2)  # Compute the dot product of two tensors
        return v0


