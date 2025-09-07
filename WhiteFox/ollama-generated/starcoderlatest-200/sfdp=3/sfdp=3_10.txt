
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.Linear(1024, 8192)
 
    def forward(self, qk):
        q = k = v = None
        q = self.attention(qk[:, :512]) # Compute the output of the linear layer with `1024` inputs and `512` outputs to compute attention weights
        k = self.attention(qk[:, 512:]) # Compute the output of the linear layer with `1024` inputs and `512` outputs to compute attention weights
        scaled_qk = torch.matmul(q, k.transpose(-2, -1)) # Compute the dot product of the query tensor and key tensor to compute the attention weights
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        return dropout_qk @ v


# Initializing the model
m = Model()

# Inputs to the model
q1 = torch.randn(5632, 4096)
k1 = torch.randn(5632, 4096)
v1 = torch.randn(5632, 8192)
qk1 = torch.cat((q1, k1), dim=0)
scaled_qk1 = qk1 @ k1.transpose(-2, -1) * scale_factor # Scale the dot product by a factor
softmax_qk1 = scaled_qk1.softmax(dim=-1) # Apply softmax to the scaled dot product
dropout_qk1 = torch.nn.functional.dropout(softmax_qk1, p=dropout_p) # Apply dropout to the softmax output
