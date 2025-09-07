
class MyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1 = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        v2 = v1.div(0.9) # Divide the output of the dot product by a constant `0.9`
        v3 = torch.nn.functional.softmax(v2, dim=-1)   # Apply softmax to the output of the dot product
        v4 = torch.nn.functional.dropout(v3, p=0.5)  # Apply dropout with the probability of 0.5 to the output of the softmax layer 
        v5 = v4.matmul(value)  # Compute the dot product between the dropout output and value tensor
        return v5


# Initializing the model
m = MyModel()
 
