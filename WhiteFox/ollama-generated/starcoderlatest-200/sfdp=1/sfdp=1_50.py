
class Attention(torch.nn.Module):
    def __init__(self, dim_query: int, dim_key: int, dim_value: int, dropout_p=0):
        super().__init__()
 
        self.linear_q = torch.nn.Linear(dim_query, dim_key) # Query layer
        self.linear_k = torch.nn.Linear(dim_key, dim_value) # Key layer
        self.linear_v = torch.nn.Linear(dim_value, dim_value) # Value layer
 
        self.dropout_q = torch.nn.Dropout(p=dropout_p)
        self.dropout_k = torch.nn.Dropout(p=dropout_p)
        self.dropout_v = torch.nn.Dropout(p=dropout_p)
 
    def forward(self, x):
        q = self.linear_q(x) # Query layer
        k = self.linear_k(x) # Key layer
        v = self.linear_v(x) # Value layer
 
        q = self.dropout_q(q)  # Apply dropout to the query layer output
        k = self.dropout_k(k)  # Apply dropout to the key layer output
        v = self.dropout_v(v)  # Apply dropout to the value layer output
 
        dot_qk = torch.matmul(q, k.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_dot_qk = dot_qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_dot_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
 
        attention = torch.nn.functional.dropout(softmax_qk, p=self._p)  # Apply dropout to the softmax output
 
        return torch.matmul(attention, v) # Compute the dot product of the attention output and the value tensor
 
    def _p(self):
        pass

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self._attn = Attention(dim_query=768, dim_key=768, dim_value=768)
 
    def forward(self, x1, x2):
        output 1 = self._attn(x1) # Apply the attention mechanism to the query and key tensor of one batch of input sequences
        output2 = self._attn(x2) # Apply the attention mechanism to the query and key tensor of one batch of input sequences
 
        return (output, output2)
 
m = Model()


# Inputs to the model
x1  = torch.randn(4096, 768)
x2 = torch.randn(4096, 768)
__output_1__, __output_2__ = m(x1, x2)

