
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_q = torch.nn.Linear(512, 8)
        self.linear_k = torch.nn.Linear(512, 8)
 
    def forward(self, x1):
        qk = torch.matmul(self.linear_q(x1), self.linear_k.transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(self.linear_v(x1)) # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 512, 64, 64)
