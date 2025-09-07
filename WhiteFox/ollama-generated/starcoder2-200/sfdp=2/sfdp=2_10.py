
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query1, key2, value3):

        v1  = torch.matmul(query1, key2.transpose(-2,-1)) # Compute the dot product of the query and the key
        v4  = torch.nn.functional.dropout(v1 / inv_scale_factor) # Apply dropout to the softmax output
        v5  = torch.matmul(v3, value)
        return v6


# Initializing the model