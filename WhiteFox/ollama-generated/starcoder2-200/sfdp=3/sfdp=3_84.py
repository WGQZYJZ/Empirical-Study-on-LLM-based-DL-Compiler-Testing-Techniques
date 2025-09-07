
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale  = torch.nn.Parameter(1) # The scale factor parameter for the dot product
        self.dropout  = torch.nn.Dropout(0.25)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value): 
        v1  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        v2  = v1 * self.scale # Scale the dot product by a factor
        v3  = v2.softmax(dim=-1) # Apply softmax to the scaled dot product
        v4  = self.dropout(v3) # Apply dropout to the softmax output
        return v4.matmul(value)


# Initializing the model