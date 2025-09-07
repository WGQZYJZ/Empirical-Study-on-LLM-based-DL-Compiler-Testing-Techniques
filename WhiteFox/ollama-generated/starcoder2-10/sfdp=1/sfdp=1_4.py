
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key, value):

        # Compute the dot product of the query and key tensors
        v1  = torch.matmul(query, key.transpose(-2, -1))
 
        # Scale the dot product by the inverse scale factor
        inv_scale_factor = key.shape[-1] ** (-0.5) 
        v2 = v1 * inv_scale_factor

        # Apply softmax to the scaled dot product and dropout
        v3  = torch.nn.functional.softmax(v2, dim=-1)
        v4  = torch.nn.functional.dropout(v3, p=0.5)

        # Compute the dot product of the dropout output and the value tensor
        v6 = v4 @ value
 
        return v6


# Initializing the model
m = Model()

# Inputs to the model
__query_ = torch.randn(1, 32, 8, 8)  # query tensor with shape [batch_size, num_heads * head_dim, sequence_length]
__key_ = torch.randn(1, 32, 4, 5)  # key tensor with shape [batch_size, num_heads * head_dim, sequence_length]
__value_ = torch.randn(1, 800, 768)  # value tensor with shape [batch_size, num_heads * head_dim, value_sequence_length]

 __output__= m(__query_, __key_, __value_)

