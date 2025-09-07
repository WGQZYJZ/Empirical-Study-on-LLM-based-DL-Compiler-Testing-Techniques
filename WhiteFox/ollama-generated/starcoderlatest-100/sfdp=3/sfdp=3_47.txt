
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8 * 4 * 4, 12)
 
    def forward(self, query_tensor, key_tensor, value_tensor):
        qk  = torch.matmul(query_tensor, key_tensor.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk  = qk.mul(scale_factor) # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output  = dropout_qk.matmul(value_tensor) # Compute the dot product of the dropout output and the value tensor
        v6     = self.linear(output).view(-1, 12) # Reshape for linear layer
        return v6
 
# Initializing the model
m = Model()
 
 # Inputs to the model
 query_tensor  = torch.randn(batch_size, num_head, sequence_length, embedding_size)
 key_tensor    = torch.randn(batch_size, num_head, sequence_length, embedding_size)
 value_tensor  = torch.randn(batch_size, num_head, sequence_length, embedding_size)
 __output__     = m(query_tensor, key_tensor, value_tensor)
 
