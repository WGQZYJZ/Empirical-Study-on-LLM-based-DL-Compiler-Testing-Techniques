
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Linear(128, 384)
 
    def forward(self, qk, v1):
        softmax_qk  = softmax(self.qkv(qk)) # Apply softmax to the dot product of query and key tensor
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the output of the previous step
        output      = torch.matmul(dropout_qk, v1) # Compute the dot product of the output of the previous step and value tensor
        return output
 

# Inputs to the model
qk = torch.randn(batch_size, 128, seq_len)
v1 = torch.randn(batch_size, 320, seq_len)
