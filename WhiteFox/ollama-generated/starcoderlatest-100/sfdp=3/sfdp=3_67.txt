
class Model(torch.nn.Module):
    def __init__(self, num_heads=8, head_dim=64, max_seq_len=128, dropout_p=0.5):
        super().__init__()
        self.num_heads = num_heads
        self.head_dim = head_dim
        self.max_seq_len = max_seq_len
        self.dropout_p = dropout_p
 
        self.key_projection = torch.nn.Linear(self.num_heads * self.head_dim, 2*self.head_dim) # Linear layer for computing the query vector and key vector of the attention mechanism. 
        self.value_projection = torch.nn.Linear(self.num_heads * self.head_dim, 2*self.head_dim) # Linear layer for computing the value tensor of the attention mechanism.
        self.dropout = torch.nn.Dropout(p=dropout_p) # Dropout with a given probability to the softmax output

    def forward(self, query, key, value):
        num_queries = query.shape[1]
        qk  = torch.matmul(query, self.key_projection.weight).transpose(-2,-1) 
        scaled_qk  = qk.mul(scale_factor) # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p) # Apply dropout to the softmax output

        num_attention_heads = self.num_heads 
        value_projection_bias  = torch.arange(0,2*num_attention_heads).unsqueeze(0)
        attention_output_tensor  = torch.einsum('b h n d, bhnd -> bhd', dropout_qk, key) # Compute the dot product of the dropout output and the value tensor 
        output  = self.dropout(attention_output_tensor + self.value_projection.weight*attention_output_tensor.transpose(-2,-1)+value_projection_bias ) # Scale the dot product by a factor
        return output


# Initializing the model
m = Model() 

# Inputs to the model
x1 = torch.randn(8, 3, 64, 64)
