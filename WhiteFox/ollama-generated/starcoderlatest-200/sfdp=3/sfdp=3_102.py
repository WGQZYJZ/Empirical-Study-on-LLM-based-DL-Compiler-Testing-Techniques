
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q = torch.nn.Linear(48, 12)
        self.k = torch.nn.Linear(48, 16)
        self.v = torch.nn.Linear(48, 16)
 
    def forward(self, q1, k1, v1):
        scaled_qk = (q1 * self.q)(query_weights).mul(scale_factor) # Compute the dot product of the query and key tensors
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        return self.v(self.k(x).matmul(self.v(torch.nn.functional.dropout((q1 * k1).mul(scale_factor), p=dropout_p)).transpose(-2, -1)))

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(8, 3, 64)
query = m.q(x)(query_weights) # Compute the query vector as a function of q and x. The weight tensor is given by query_weights
key   = m.k(torch.randn(16))    # Compute the key vector as a function of k and x. The input tensor x will be reused in k.
value = m.v(x)                   # Compute the value vector as a function of v and x. This time, we don't use dropout. 
