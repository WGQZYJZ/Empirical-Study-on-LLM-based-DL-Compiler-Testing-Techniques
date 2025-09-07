
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.query = torch.nn.Linear(768, 3072)
        self.key = torch.nn.Linear(768, 3072)
        self.value = torch.nn.Linear(768, 3072)
 
    def forward(self, query_x1):
        query = self.query(query_x1)
        key = self.key(query_x1)
        value = self.value(query_x1)
 
        qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and the key
        scaled_qk = qk.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value
        return output


# Inputs to the model
query_x1 = torch.randn(1, 768)
