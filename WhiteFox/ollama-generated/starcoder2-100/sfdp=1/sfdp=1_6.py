

class AttentionBlock(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(64, 32)
        self.key = torch.nn.Linear(128, 64)
        self.value = torch.nn.Linear(192, 128)
 
    def forward(self, x):
        qk = torch.matmul(query(x), key(x).transpose(-2, -1)) / scale_factor # Compute the dot product of the query and key tensors
        scaled_qk = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        return dropout_qk.matmul(value(x))
 

class Model(torch.nn.Module):
    def __init__(self):
         super().__init__()
         self.attn1 = AttentionBlock()
         self.attn2 = AttentionBlock()
 
    def forward(self, x):
        v1  = attn1(x)
        v2  = attn2(v1)
        return v2

# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(64, 3072)
__output__  = m(x1)


