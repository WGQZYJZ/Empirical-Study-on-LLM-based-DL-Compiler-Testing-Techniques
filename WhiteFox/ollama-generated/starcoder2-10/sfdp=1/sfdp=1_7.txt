
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.randn(1024, 35)
        self.key = torch.randn(35, 768)
        self.value = torch.randn(19, 768)
 
    def forward(self):
        v1 = torch.matmul(self.query, self.key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        v3 = self.value
        v4 = torch.div(v1, 0.7598) # Scale the dot product by 0.7598
        v6 = softmax(v4, dim=-2) # Apply softmax to the scaled dot product with dimension -2
        v7 = torch.nn.functional.dropout(v3) # Apply dropout to the value tensor
        