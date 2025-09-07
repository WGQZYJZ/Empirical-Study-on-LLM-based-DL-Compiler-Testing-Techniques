
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(32, 8)
 
    def forward(self, x1):
        qk = torch.matmul(x1, x1.transpose(-2, -1))  # Compute the dot product of each input vector with itself
        q = F.softmax(qk, dim=-1)  # Apply softmax to the query matrix
        v = self.attn(x1)  # Compute the linear projection of the value tensor onto the hidden states of the attention mechanism
        dropout_v = F.dropout(q * v, p=dropout_p, training=training)  # Apply dropout to the projections obtained from the softmax and the value tensors
        return dropout_v


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
