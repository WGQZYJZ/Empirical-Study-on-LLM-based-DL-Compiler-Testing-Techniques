
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q = torch.nn.Linear(1024, 128) 
        self.k = torch.nn.Linear(1024, 128)
        self.v = torch.nn.Linear(1024, 128)
 
    def forward(self, q, k):
        q_emb = self.q(q) # Project the query by using a linear transformation and the key embedding matrix 
        v_emb = self.v(k) # Project the value by using a linear transformation and the key embedding matrix
        attn = torch.matmul(q_emb, k.transpose(-2, -1)) # Compute the dot product of the query and key tensor
        scaled_attn = attn.mul(scale_factor) # Scale the dot product by a factor 
        softmax_attn = scaled_attn.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_attn = torch.nn.functional.dropout(softmax_attn, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_attn.matmul(v_emb) # Compute the dot product of the dropout output and the value tensor
        return output

# Inputs to the model
query = torch.randn(1024, 1024)
key = torch.randn(1024, 1024)
