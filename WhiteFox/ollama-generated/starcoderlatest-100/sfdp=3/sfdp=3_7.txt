
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_q = torch.nn.Linear(d, d)  # Compute the dot product between the query tensor and the key tensors of shape (batch_size, seq_len, head_num * d_model / head_dim, 1)
        self.attn_k = torch.nn.Linear(d, d)  # Compute the dot product between the query tensor and the key tensors of shape (batch_size, seq_len, head_num * d_model / head_dim, 1)
        self.attn_v = torch.nn.Linear(d, d)  # Compute the dot product between the query tensor and the value tensors of shape (batch_size, seq_len, head_num * d_model / head_dim, 1)
        self.attn_o = torch.nn.Linear(d, d)
 
    def forward(self, q):
        x0 = q # store original query
        qk  = self.attn_q(x0)
        k = self.attn_k(qk).reshape(qk.shape[0], -1, 1, 1)
        v = self.attn_v(qk).reshape(qk.shape[0], -1, 1, 1)
        attn = qk @ k.transpose(-2, -1) # compute attention with shape (batch_size, seq_len, head_num * d_model / head_dim, seq_len)
        softmax_attn = torch.nn.functional.softmax(attn, dim=-1)
        x1 = torch.nn.functional.dropout(softmax_attn, p=0.25, training=self.training) # apply dropout with prob 0.25 to the output of the attention operation
        output = (x1 @ v).squeeze(dim=-1)
        output = self.attn_o(output) + x0
        return output


# Initializing the model
m = Model()

# Inputs to the model
q = torch.randn(32, 8, d) # store original query of shape (batch_size, seq_len, head_num * d_model / head_dim)
