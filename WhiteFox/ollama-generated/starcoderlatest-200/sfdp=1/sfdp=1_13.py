
class Model(torch.nn.Module):
    def __init__(self, d_k=64, d_v=128, max_num_key_values=None, max_query_depths=3, max_attention_heads=1):
        super().__init__()
        self.qkv = torch.nn.Linear(d_model=d_k*3, out_features=(d_k*3 + d_v)*max_num_key_values)
 
    def forward(self, x1):
        q  = torch.tanh(x1[:, :self.dim], dim=-2) # First tanh applied on the queries
        v  = torch.tanh(x1[:, self.dim:2*self.dim], dim=-2) # Second tanh applied on the values
        k  = torch.tanh(x1[:, 2*self.dim:], dim=-2) # Third tanh applied on the keys
 
        qk  = torch.einsum('bthd,btcj->btci', (q, k)) # Dot product of queries and keys
        scaled_qk  = qk / self.inv_scale_factor # Scale the dot product by the inverse scale factor
        softmax_qk  = torch.softmax(scaled_qk, dim=-1) # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p) # Apply dropout to the softmax output
        output  = dropout_qk @ v # Dot product of the dropout output and the values
        
        return output
 
    def get_input_dimension(self):
        self.dim = int(self.qkv.out_features/3)


# Initializing the model
m = Model()
m.get_input_dimension()
