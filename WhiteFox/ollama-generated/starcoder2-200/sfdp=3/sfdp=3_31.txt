
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = 0.23456789101  # Set the scale factor to 0.23456789101
        self.dropout_p = 0.423
        
    def forward(self, query, key):
        v1 = torch.matmul(query, key)
        v2 = v1 * self.scale
        v3 = torch.softmax(v2, dim=-1) # Applies softmax to the scaled dot product
        v4 = torch.nn.functional.dropout(v3, p=self.dropout_p)  # Applies dropout to the softmax output
        v5 = v4 * value
        return v5


# Initializing and using the model