
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Linear(8, 3)
 
    def forward(self, x1):
        v1  = self.qkv(x1).chunk(3, dim=-1)
        v2  = torch.matmul(v1[0], v1[1].transpose(-2, -1)) # Compute the dot product of a query and a key
        inv_scale  =  8.0
        v3  = (v2 / inv_scale).softmax(dim=-1) # Scale the dot product by an inverse scale factor
        inv_scale  = float(self.qkv.weight[0][0]) * float(self.qkv.weight[1][0]) / float(inv_scale**(-3)) # Compute the value of the inverse scale factor based on the weights of qkv
        v4  = torch.nn.functional.dropout(v3, p=float(self.qkv.weight[-2]))  # Apply dropout to the softmax output with dropout probability set by the weights of qkv's last weight
        inv_scale  /= float(inv_scale**(-1)) * v4 # Scale the output by an inverse scale factor
        v5 = torch.matmul(v4, v1[2])  # Compute the dot product of a dropout output and a value based on the original query, key, value inputs to the model
        return (v5, inv_scale)


# Initializing the model
m  = Model()


# Inputs to the model