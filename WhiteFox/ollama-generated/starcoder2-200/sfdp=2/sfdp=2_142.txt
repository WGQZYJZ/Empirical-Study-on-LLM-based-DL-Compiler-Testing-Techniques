
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.functional.dropout
 
    def forward(self, query1, key2, value3):
        vq  = self.matmul(query1 @ key2.transpose(-2, -1), p=0) # Compute the dot product of the query and the key
        vs  = vq / np.sqrt(486.5579834)   # Scale the dot product by the inverse scale factor
        vo  = vs.softmax(dim=-1).matmul(value3)  # Apply softmax to the scaled dot product then compute the dot product of the dropout output and a value
        return vo


# Initializing model
m = Model()

# Inputs for the model
q, k, v  = [torch.randn(2001, 486) for i in range(3)] # The number is arbitrary and not limited to the length of q, k, and v (or key, value, query). 
__output__  = m(q, k, v)