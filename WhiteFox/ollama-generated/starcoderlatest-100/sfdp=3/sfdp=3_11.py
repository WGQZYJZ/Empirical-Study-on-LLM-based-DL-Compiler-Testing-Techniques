
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk * scale_factor  # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
query = torch.randn(1, 256, 192, 80) # The shape is [batch size, sequence length (L), input size (N), hidden size (H)]
key = torch.randn(256, 256, 7, 7) # The shape is [attention heads (H), attention head size (A), query embedding dimension, key embedding dimension]
value = torch.randn(256, 256, 192, 80) # The shape is [batch size, sequence length (L), input size (N), hidden size (H)]


