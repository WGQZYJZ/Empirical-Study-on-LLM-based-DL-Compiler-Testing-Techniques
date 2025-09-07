
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention_module = torch.nn.MultiheadAttention(3, 8)
 
    def forward(self, x1, x2):
        qk = self.attention_module(x1, x2, x2)[0] # Compute the attention scores of the input query and key tensors
        scaled_qk = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 8, 64, 64)
x2 = torch.randn(4, 3, 64, 64)
