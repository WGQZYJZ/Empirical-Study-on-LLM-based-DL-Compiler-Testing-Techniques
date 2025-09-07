
class Attention(torch.nn.Module):
    def __init__(self, dim_q=32, dim_k=32, dim_v=16):
        super().__init__()
        self.dim_q = dim_q
        self.dim_k = dim_k
        self.dim_v = dim_v
 
        self.w_q = torch.nn.Linear(dim_q, dim_k)
        self.w_k = torch.nn.Linear(dim_k, dim_k)
        self.w_v = torch.nn.Linear(dim_k, dim_v)
 
    def forward(self, qk):
        v  = torch.matmul(qk, self.w_v.weight).transpose(-2, -1)
        w_q  = torch.nn.functional.relu(self.w_q(qk))
        softmax_qk  = torch.nn.functional.softmax(w_q, dim=-1)
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output  = dropout_qk.matmul(self.w_v.weight).transpose(-2, -1)
        return output
 
    def forward_train(self, query, key):
        qk = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(scale_factor)  # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value tensor
        return output
 
 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention1 = Attention(dim_q=32, dim_k=64, dim_v=64)
 
    def forward(self, x1):
        attention_output = self.attention1(qk) # Apply the forward function of the attention module on query and key tensors
        return attention_output
 
# Initializing the model
m = Model()
 
 # Inputs to the model
x1 = torch.randn(1, 32, 64, 64)
