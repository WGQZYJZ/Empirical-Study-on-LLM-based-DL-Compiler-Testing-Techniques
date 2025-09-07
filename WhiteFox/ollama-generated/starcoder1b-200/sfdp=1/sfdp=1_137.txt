
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 4)
        self.key = torch.nn.Linear(4, 5)
        self.value = torch.nn.Linear(5, 6)
 
    def forward(self, query_tensor, key_tensor, value_tensor):
        qk = torch.matmul(query_tensor, key_tensor.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(value_tensor)  # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()

