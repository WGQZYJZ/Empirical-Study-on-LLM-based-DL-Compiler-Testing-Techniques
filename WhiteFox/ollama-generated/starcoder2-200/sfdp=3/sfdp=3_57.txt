
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key1, value1, scale_factor=2048.0, dropout_p=0.5):
        v = torch.matmul(query1, key1.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        v2 = v.mul(scale_factor)  # Scale the dot product by a factor
        softmax_v3 = v2.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_softmax4 = torch.nn.functional.dropout(softmax_v3, p=dropout_p)  # Apply dropout to the softmax output
        return dropout_softmax4.matmul(value1)


# Initializing the model