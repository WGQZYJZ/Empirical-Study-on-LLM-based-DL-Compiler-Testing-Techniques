
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1, k1, v1):
        qk = torch.matmul(q1, k1.transpose(-2, -1)) # Compute the dot product of query and key tensors
        scaled_qk  = qk * scale_factor
        softmax_qk  = scaled_qk.softmax(dim=-1) 
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the output of the softmax
        output = dropout_qk.matmul(v1)   # Compute the dot product of the result of dropout and the value tensor
        return output

# Initializing a model with some random weights/tensors: 
m  = Model()

