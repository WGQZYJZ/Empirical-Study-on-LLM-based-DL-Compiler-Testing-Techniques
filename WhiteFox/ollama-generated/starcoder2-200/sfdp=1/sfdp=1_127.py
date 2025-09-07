

class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.dropout = torch.nn.Dropout(p=0)
        self.scale  = torch.nn.Parameter(torch.ones([1]))
 
    def forward(self, query_tensor, key_tensor, value_tensor, dropout_p=None):
            # Initialize the scale factor based on the given constant value (default to be 64).
            inv_scale_factor = self.scale.expand([-1]) ** (-0.5)
 
            qk  = torch.matmul(query_tensor, key_tensor.transpose(-2, -1)) # Compute the dot product of the query and key tensors
            scaled_qk = qk.div_(inv_scale_factor)    # Scale the dot product by the inverse scale factor
            softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
 

            if dropout_p is not None:
                dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p)    # Apply dropout to the softmax output
            else:
                dropout_qk  = softmax_qk
 
            output   = dropout_qk.matmul(value_tensor) # Compute the dot product of the dropout output and the value tensor
 
            return output

# Initializing the model