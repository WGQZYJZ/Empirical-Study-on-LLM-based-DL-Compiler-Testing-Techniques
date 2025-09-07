
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key2, value3):
        v1 = torch.matmul(query1, key2.transpose(-2, -1))  # Compute the dot product of two tensors
        v2 = v1 * scale_factor
        v3 = v2.softmax(dim=-1) 
        v4 = torch.nn.functional.dropout(v3, p=dropout_p) # Apply dropout to the softmax output
        v5 = v4.matmul(value3)  # Compute the dot product of the dropout output and another tensor value

        return v5

# Initializing the model
m = Model()
 
# Inputs to the model
k1 = torch.randn(20, 60, 97, 97).transpose(-2, -1) # Define a tensor that represents keys
k2 = k1 + torch.randn_like(k1) * 3 / 8
v1 = torch.randn(40, 50, 97, 97)
 
query1  = v1[:20]
query2 = query1 + torch.randn_like(query1).mul_(0.05)
query3 = query2 - torch.randint(low=1, high=48, size=[20])
key2 = k2[:, 19:]
value3 = v1[:, :6]
 
