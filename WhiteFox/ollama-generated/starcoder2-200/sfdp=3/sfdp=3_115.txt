
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.randn(3, 4)
        self.key   = torch.randn(3, 4)
        self.value  = torch.randn(3, 5)
 
    def forward(self, scale_factor=0.78):
        v1  = self.query
        v2  = self.key.transpose(-2, -1) # Switching the tensor dimensions is a common practice in PyTorch
        v3  = torch.matmul(v1, v2) # Computing dot product of the query and key tensors
        v4  = v3 * scale_factor 
        v5  = v4.softmax(dim=-1) # Applying softmax to scaled dot products
        v6  = torch.nn.functional.dropout(v5, p=0.78923078) # Dropout is a common practice in PyTorch
        v7  = v6.matmul(self.value)# Multiply the dropout output and value tensors
        return v7


# Initializing the model: 
m = Model()
