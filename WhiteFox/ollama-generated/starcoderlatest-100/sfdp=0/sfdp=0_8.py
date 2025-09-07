
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, d_model, dropout=0.1):
        super().__init__()
        self.dropout = torch.nn.Dropout(p=dropout)
        self.q_dense = torch.nn.Linear(d_model, d_model) # Query Dense Layer (No activation layer)
        self.k_dense = torch.nn.Linear(d_model, d_model) # Key Dense Layer (No activation layer)
        self.v_dense = torch.nn.Linear(d_model, d_model) # Value Dense Layer (No activation layer)

    def forward(self, q, k, v):
        # Shape of the attention matrix: [batch_size, num_heads, seq_len, head_dim] 
        matmul_qk = torch.matmul(q, self.q_dense(k)) 
        
        scaled_attention_logits = matmul_qk / math.sqrt(d_model)
        attention_weights = torch.softmax(scaled_attention_logits, dim=-1) # No activation function

        out = torch.matmul(self.dropout(attention_weights), v) # Batch matrix multiplication 

        return out, attention_weights


# Initializing the model
sdpa = ScaledDotProductAttention(d_model)


# Inputs to the model
q = torch.randn(1, 8, d_model)
k = torch.randn(2, 8, d_model)
v = torch.randn(2, 8, d_model)
__output__, __attention_weights__ = sdpa(q, k, v)


# Please also generate the attention weights for the newly generated model. You can use the code snippet provided in `scaled-dot-product-attention/main.py` as a reference.