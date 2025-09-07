
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale  = torch.nn.Parameter(torch.randn(()))
        self.dropout  = torch.nn.Dropout(p=0.1)
 
    def forward(self, query, key, value):
        v1 = torch.matmul(query, key.transpose(-2, -1)) * scale_factor # Compute the dot product of the query and key tensors
        v2  = self.dropout(v1).softmax(dim=-1)# Apply dropout to the softmax output
        return v2.matmul(value)

# Initializing model
m = Model()

