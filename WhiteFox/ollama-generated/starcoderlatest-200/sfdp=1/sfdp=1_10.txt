
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.Linear(3, 8, bias=False)
 
    def forward(self, q, k):
        v = self.matmul(k)  # Compute the dot product of the key tensor and a value tensor
        return torch.matmul(q, v).softmax(dim=-1)


# Inputs to the model
query = torch.randn(1, 3, 64, 64)
key   = torch.randn(1, 8, 64, 64)
