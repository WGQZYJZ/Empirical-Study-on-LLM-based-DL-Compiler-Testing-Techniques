

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.nn.Linear(64, 32) # Create a linear layer with output size 32 and input size 64

    def forward(self, query, key):
        v1 = torch.matmul(query, key.transpose(-2,-1))# Compute the dot product of two tensors
        v2 = v1 / scale_factor  # Scale by an inverse scale factor
        v3 = v2.softmax(dim=-1)  # Apply softmax to scaled dot products 
        v4 = torch.nn.functional.dropout(v3, p=dropout_p)# Apply dropout with probability p for each tensor element
        v5 = v4 @ value  # Compute the dot product of dropout output and another tensor. 
        return v5


# Initializing the model