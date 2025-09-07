
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, qk1, qk2, key):  # Inputs: query tensor and dropout probability `p` as well as the key tensor for computing the dot product with the value tensor
        scaled_qk = torch.matmul(qk1, qk2) / inv_scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Compute the softmax of the scaled dot product of query and key tensors
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.35)  # Apply dropout to the output of the softmax
        output = dropout_qk.matmul(key)  # Compute the dot product of dropout output with value tensor
        return output


# Initializing the model
m = Model()
 
 # Inputs to the model
qk1 = torch.randn(32, 4096).cuda()
qk2 = torch.randn(512, 8)
key = torch.rand(16, 512, 768)

 # Initializing a dropout probability `p` with a value greater than zero and smaller than one.
dropout_p = 0.3
 
# Scale factor of the dot product
scale_factor = 4
 
 # Inverse scale factor is obtained by dividing the scale factor by the scaling constant
inv_scale_factor = inv_scale / scale_factor

 # The output of the model when inputting query tensors, dropout probability `p`, and key tensor are computed.
output  = m(qk1, qk2, key)
 
