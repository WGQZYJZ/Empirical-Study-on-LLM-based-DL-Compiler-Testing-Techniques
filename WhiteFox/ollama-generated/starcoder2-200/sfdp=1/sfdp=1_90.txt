
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key, value):
        v1 = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scale_factor = 0.5  # Assign a fixed scale factor to scale the dot product by
        scaled_v1 = v1 / scale_factor  # Scale the dot product by the fixed scale factor
        v2 = scaled_v1.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_p = 0.75  # Assign a fixed dropout probability p to apply dropout to the softmax output
        v3 = torch.nn.functional.dropout(v2, p=dropout_p)  # Apply dropout to the softmax output with the fixed p value

        v4 = v3.matmul(value) 
        return v4


# Initializing the model