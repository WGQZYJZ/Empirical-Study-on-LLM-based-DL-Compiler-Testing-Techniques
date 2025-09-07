
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, n_head, d_k, d_v, dropout=0.1):
        super().__init__()
        self.n_head = n_head
        self.d_k = d_k
        self.d_v = d_v
 
        # Parameters of the multihead attention module are concatenated together 
        # as a single parameter for simplicity of implementation; therefore, 
        # the two layers of parameters are concatenated here
        self.q_layer = torch.nn.Linear(d_model, n_head * d_k)
        self.k_layer = torch.nn.Linear(d_model, n_head * d_k)
        self.v_layer = torch.nn.Linear(d_model, n_head * d_v)
 
        # Split off the heads to allow for separate attention weights 
        # with each head being used as a linear layer output
        self.q_head = torch.nn.Linear(n_head * d_k, n_head, bias=False)
        self.k_head = torch.nn.Linear(n_head * d_k, n_head, bias=False)
        self.v_head = torch.nn.Linear(n_head * d_v, n_head, bias=False)
 
        # Final linear layer with a single output for use in classification or other downstream tasks
        self.dense = torch.nn.Linear(n_head * d_v, 1)
 
        # Apply dropout to the final layer of each block
        self.dropout = torch.nn.Dropout(p=dropout)
 
    def forward(self, x):
        batch_size = x.shape[0]
        n_q, n_k, n_v = x.shape[1:4]
 
        # Apply linear transformation to the query and key
        q = self.q_layer(x).view([batch_size, -1, self.n_head, self.d_k])
        k = self.k_layer(x).view([batch_size, -1, self.n_head, self.d_k])
 
        # Compute attention on the query and key
        attn  = torch.matmul(q, k.transpose(-2,-1)) # Attention score is a matrix multiplication between the two sets of input vectors.
        
        # Scale the dot product by inverse scale factor to prevent underflow 
        inv_scale_factor = self.d_k ** -0.5
 
        attn = attn.div(inv_scale_factor)
        attn = torch.nn.functional.softmax(attn, dim=-1).mul(1e20).add(-1e20)
 
        # Dropout for input vectors during the self-attention stage
        # https://arxiv.org/pdf/1905.03197v2.pdf
        attn = self.dropout(attn)
 
        # Apply linear transformation to get attention weights on value set 
        v = self.v_layer(x).view([batch_size, -1, self.n_head, self.d_v])
 
        # Compute the output using weighted sum of values
        attn_values = torch.matmul(attn, v)
 
        # Split off the heads so that each head can be applied as a linear layer 
        attn_values = attn_values.transpose(-2,-1).contiguous().view([batch_size, -1, self.n_head * self.d_v])
        out = self.dense(attn_values)
 
        # Dropout to prevent overfitting during classification 
        out = self.dropout(out)
 
        # Apply the same linear transformation on the query and key heads 
        q = self.q_head(q).transpose(-2,-1)
        k = self.k_head(k).transpose(-2,-1)
 
        # Compute attention score for values
        attn = torch.matmul(q, k.transpose(-2,-1))
        attn = attn.div(inv_scale_factor)
 
        # Apply softmax and add epsilon to prevent underflow 
        attn = torch.nn.functional.softmax(attn, dim=-1).add(1e-8)
 
        # Dropout for input vectors during the self-attention stage
        # https://arxiv.org/pdf/1905.03197v2.pdf
        attn = self.dropout(attn)
 
        # Apply linear transformation to get attention weights on value set 
        v = self.v_head(v).transpose(-2,-1)
 
        # Compute the output using weighted sum of values
        attn_values = torch.matmul(attn, v)
 
        # Split off the heads so that each head can be applied as a linear layer 
        attn_values = attn_values.view([batch_size, -1, self.n_head * self.d_v])
        out += self.dense(attn_values)
 
        return out


# Initializing the model
m = MultiHeadAttention(20, 64, 32, dropout=0.5)

