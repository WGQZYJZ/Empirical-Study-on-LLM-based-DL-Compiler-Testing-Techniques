
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, num_heads=8, key_dim=256, dropout_p=0.1):
        super().__init__()
        self.num_heads = num_heads
        self.key_dim = key_dim
 
        # Define the number of dimensions for a given head in order to compute its weight tensor
        inner_head_dim = (self.key_dim + 7) // 8 * 8
 
        # Linear layers to compute the multi-head dot product and scaled dot product
        self.q_lin1 = torch.nn.Linear(256, inner_head_dim)
        self.k_lin2 = torch.nn.Linear(256, inner_head_dim)
        self.v_lin3 = torch.nn.Linear(256, inner_head_dim)
 
        # Linear layers to compute the softmax output and dropout
        self.scale_factor = math.sqrt(self.key_dim)
        self.attn_output_lin4 = torch.nn.Linear(inner_head_dim * self.num_heads, 256)
        self.dropout_lin5 = torch.nn.Linear(256, 256)
 
        # Define the final output linear layer and a dropout layer
        self.final_output_lin6 = torch.nn.Linear(256, 1000)
 
    def forward(self, x):
        # Linear transformation to obtain multiple heads from a single input tensor
        query = self.q_lin1(x)
        key = self.k_lin2(x)
        value = self.v_lin3(x)
 
        # Concatenate the query and key tensors in order to obtain all multi-head attention vectors for all heads at once
        concat_query_key  = torch.cat([query, key], dim=-1)
 
        # Linear transformation to compute a single multi-head dot product for each head
        qk = self.q_lin1(concat_query_key)
        kq = self.k_lin2(concat_query_key)
        vq = self.v_lin3(concat_query_key)
 
        # Concatenate the key tensor and all multi-head dot products for all heads at once
        concat_kq = torch.cat([key, qk], dim=-1)
 
        # Compute a single multi-head dot product between the query and every multi-head attention vector in order to obtain each attention weight for each head
        attn_weights = self.scale_factor * torch.matmul(vq, concat_kq.transpose(-2, -1))
        softmax_attn_weights = attn_weights.softmax(dim=-1)
 
        # Apply dropout between the linear transformation and the subsequent linear transformation to obtain a multi-head attention output tensor
        dropout_attn_weights = self.dropout_lin5(torch.nn.functional.relu(self.attn_output_lin4(attn_weights)))
 
        # Concatenate all multi-head attention outputs for all heads into a single tensor by stacking the individual attention weights together and then applying softmax to obtain the attention probabilities
        attention_probs = torch.matmul(dropout_attn_weights, value).squeeze(-2)
        attention_probs  = attention_probs.softmax(dim=-1)
 
        # Apply dropout between the linear transformation and the subsequent linear transformation in order to obtain a single output tensor
        dropout_attention_probs = self.dropout_lin5(torch.nn.functional.relu(self.final_output_lin6(attention_probs)))
 
        # Compute the dot product of each query embedding with its corresponding multi-head attention weights vector by using multiple linear layers between the input query tensor and the multi-head attention weights tensor
        output = self.final_output_lin6(dropout_attention_probs)
 
        return output
# Inputs to the model
x1 = torch.randn(1, 3, 256, 256)
m = MultiHeadAttention()
