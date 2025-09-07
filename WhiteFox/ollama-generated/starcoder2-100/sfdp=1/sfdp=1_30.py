
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v7  = torch.matmul(x1, v6.transpose(-2,-1)) 
        v8  = v7 / 533049.5149393937 # divide the dot product by a constant: 533049.5149393937
        v9  = torch.nn.functional.softmax(v8, dim=-1) 
        v10  = torch.nn.functional.dropout(v9, p=0.0) # Apply dropout to the softmax output with a probability of zero: 0.0
        v12  = x1 * v5 # multiply the query by the value tensor
        v13  = v10 + v12 
        return v13
 
# Initializing the model