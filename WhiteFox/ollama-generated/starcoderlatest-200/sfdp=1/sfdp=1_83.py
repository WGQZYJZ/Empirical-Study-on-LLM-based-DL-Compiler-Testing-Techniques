
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(128, 64)
 
    def forward(self, query_x1, key_x1, value_x1):
        qk = torch.matmul(query_x1, key_x1.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk / scale_factor # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(value_x1) # Compute the dot product of the dropout output and the value tensor
        return output


# Inputs to the model
query_x1 = torch.randn(256, 128)
key_x1 = torch.randn(128, 128)
value_x1 = torch.randn(256, 128)
