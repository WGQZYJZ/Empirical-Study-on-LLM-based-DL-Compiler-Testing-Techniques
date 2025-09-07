
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query_vec, key_vecs, value_vecs):
        qk = torch.matmul(query_vec, key_vecs.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        return dropout_qk.matmul(value_vecs)


# Initializing the model
m = Model()

query_vec = torch.randn(batch_size * beam_size, query_len, d_model)  # Inputs to the model for queries
key_vecs = torch.randn(beam_size * block_size, key_len, d_model)  # Inputs to the model for keys


