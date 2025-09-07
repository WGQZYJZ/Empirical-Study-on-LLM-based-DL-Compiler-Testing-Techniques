
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 512)
        self.softmax = torch.nn.Softmax()
 
    def forward(self, x1, x2):
        # v1  = torch.matmul(x1, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        # scaled_v1 = v1.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        # softmax_v1 = self.softmax(scaled_v1) # Apply softmax to the scaled dot product
        qk  = torch.matmul(x2, x1.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = self.softmax(scaled_qk) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value tensor
        return output


# Inputs to the model
x1  = torch.randn(128, 128)
x2  = torch.randn(128, 128)
