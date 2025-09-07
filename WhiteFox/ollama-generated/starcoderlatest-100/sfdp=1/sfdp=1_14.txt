
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, inv_scale_factor, dropout_p):
        qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()


# Inputs to the model
query = torch.randn(8, 256, 64, 64)  # Input tensor
key = torch.randn(16, 256, 64, 64)  # Input tensor
value = torch.randn(8, 128, 64, 64)  # Input tensor
inv_scale_factor = torch.tensor([0.5])  # Constant to be multiplied by the dot product of a query and key tensor before applying softmax
dropout_p = torch.__fmod__(torch.randn(1).item(), 0.975)  # Float32 random number in range [0.95, 1] to control dropout probability
