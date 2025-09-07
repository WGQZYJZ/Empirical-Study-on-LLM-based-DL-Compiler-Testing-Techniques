class MyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key):
        # Compute the scaled dot product of the query and key tensors.
        query = torch.softmax(query @ key.transpose(-2, -1), dim=-1)
 
        # Compute a weighted sum of values using attention weights.
        value  = ...
 
        return value
