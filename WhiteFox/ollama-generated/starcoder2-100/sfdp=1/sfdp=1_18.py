
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key1, value1):
        v  = torch.matmul(query1, key1)  # Compute the dot product of two tensors
        return v

