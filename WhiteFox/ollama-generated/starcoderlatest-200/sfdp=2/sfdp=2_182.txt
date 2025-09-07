
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_q = torch.nn.Linear(d_model, d_ff)
        self.linear_k = torch.nn.Linear(d_model, d_ff)
        self.linear_v = torch.nn.Linear(d_model, d_ff)
 
    def forward(self, query, key, value):
        q1 = F.relu(self.linear_q(query)) # Compute the output of a Linear layer with input size (batch x 2048 x 64 x 64), and linear_q has size (2048, 1) 
        k1 = F.relu(self.linear_k(key))
        v1 = self.linear_v(value)
 
        q1 = torch.nn.functional.permute(q1, (0, 3, 1, 2)) # Compute the output of a permutation operation on input tensor with dimension permutation (0, 3, 1, 2). 
        k1 = torch.nn.functional.permute(k1, (0, 3, 1, 2))
        v1 = torch.nn.functional.permute(v1, (0, 3, 1, 2))
 
        q1 = torch.nn.functional.reshape(q1, (b_size, d_ff, -1)) # Compute the output of a reshape operation on input tensor with shape (batch x 2048 x (64 x 64)).
        k1 = torch.nn.functional.reshape(k1, (b_size, d_ff, -1))
        v1 = torch.nn.functional.reshape(v1, (b_size, d_ff, -1))
 
        dot_product = torch.einsum('bnw,bnm->bnd', q1, k1)  # Compute the output of a matrix multiplication operation on input tensors with dimension permutation (0, 3, 1, 2), and equation size: bnw x bn m d n, which means b_size x d_ff x 64 x 64 x 64 = batch_size x 2048 x 64 x 64
        scaled_dot_product = dot_product.div(1 / math.sqrt(d_ff)) # Scale the output of matrix multiplication operation by (1 / sqrt(d_ff))
 
        attention_score = torch.nn.functional.softmax(scaled_dot_product, dim=-1)  # Apply softmax to the scaled dot product
        attention_score = self.dropout(attention_score)  # Dropout for regularization
        weighted_sum = torch.einsum('bnd,bnm->bnw', attention_score, v1)  # Compute the output of a matrix multiplication operation on input tensors with dimension permutation (0, 3, 1, 2), and equation size: bnd x bn m d n, which means batch_size x 2048 x 64 x 64 x 64 = batch_size x 2048 x 64 x 64
        weighted_sum = torch.nn.functional.reshape(weighted_sum, (b_size, -1)) # Compute the output of a reshape operation on input tensor with shape (batch x (64 x 64)), where b_size equals batch size
        
        