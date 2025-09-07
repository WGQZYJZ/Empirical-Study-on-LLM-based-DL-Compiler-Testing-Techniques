
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Linear(8, 32)
 
    def forward(self, qk, x1):
        v1  = self.qkv(qk).split(32, dim=-1)
        key_tensor, query_tensor, value_tensor = torch.stack((v1[0], v1[1], v1[2])), torch.stack((v1[3], v1[4], v1[5])), v1[6]
        scaled_qk  = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(value_tensor)  # Compute the dot product of the dropout output and the value tensor
        return output


# Model Initialization
m1 = Model()
m2 = Model()

# Inputs to the model
qk = torch.randn(8, 64, 64) # Shape: (8, 64, 64)
x1 = torch.randn(1, 3, 64, 64) # Shape: (1, 3, 64, 64)

