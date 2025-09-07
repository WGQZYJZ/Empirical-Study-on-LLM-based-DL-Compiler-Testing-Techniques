
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.matmul = torch.nn.Linear(128, 32)
 
    def forward(self, x1, x2):
        # Get the output of matmul module by computing the dot product between query tensor and key tensor
        qk = torch.matmul(x1, x2.transpose(-2, -1))
 
        # Scale the dot product by inverse scale factor
        scaled_qk  = qk / inv_scale_factor

        # Apply softmax to the scaled dot product
        softmax_qk = torch.softmax(scaled_qk, dim=-1)

        # Apply dropout to the softmax output
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)

        # Compute the dot product of the dropout output and value tensor
        output = dropout_qk.matmul(x2)
        return output


# Initializing the model
m = Model()
 
# Inputs to the model
x1  = torch.randn(batch_size, nhead, query_len, d_k)
x2  = torch.randn(batch_size, nhead, key_len, d_v)
 
