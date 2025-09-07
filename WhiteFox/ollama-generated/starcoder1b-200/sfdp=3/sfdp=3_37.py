
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 4)
        self.key = torch.nn.Linear(3, 4)
        self.value = torch.nn.Linear(2, 4)
 
    def forward(self, query_tensor, key_tensor):
        scale_factor  = (torch.sqrt(self.key.weight[0]).reshape(-1, 1, 1) *
                          self.value.weight.t()).unsqueeze(dim=-1).expand(query_tensor.shape[:-2])
        dropout_p     = dropout_rate  # Dropout probability for this specific operation.
        qk           = torch.matmul(query_tensor, key_tensor.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk    = qk.mul(scale_factor)  # Scale the dot product by a factor
        softmax_qk   = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk   = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output       = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value tensor
        return output


# Inputs to the model
q1  = torch.randn(1, 4, 64, 64)
k1  = torch.randn(1, 4, 64, 64)
v1  = torch.randn(1, 2, 64, 64)
