
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1 = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        v2 = v1 / scale_factor
        v3 = v2.softmax(dim=-1)
        v4 = torch.nn.functional.dropout(v3, p=dropout_p)
        return v4.matmul(value)


# Initializing the model
m  = Model()
 
 # Inputs to the model
query  = torch.randn(256, 789, 1024).float()
key  = torch.randn(256, 1024, 512).float()
value  = torch.randn(256, 512, 100)
 
__output__  = m(query, key, value)

# Sample input for the model
query  = torch.rand(32, 789, 1024).float()
key  = torch.rand(32, 1024, 512).float()
value  = torch.rand(32, 512, 100).float()

