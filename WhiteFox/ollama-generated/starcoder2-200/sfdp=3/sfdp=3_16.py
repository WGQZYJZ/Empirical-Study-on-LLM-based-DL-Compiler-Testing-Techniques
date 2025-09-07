
class SelfAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.query = torch.nn.Parameter(
            data=torch.zeros(32, 512), requires_grad=True)
        self.key   = torch.nn.Parameter(
            data=torch.zeros(8,   32, 512), requires_grad=True)
        self.value = torch.nn.Parameter(data=torch.zeros(8, 32, 512))
 
    def forward(self):
        scale_factor = 0.7978  # A scaling factor that is not a constant but depends on the model
        dropout_p    = 0.6   # An element-wise dropout probability
        
        query         = self.query       # Retrieve the query tensor from parameters in the model
        key           = self.key        # Retrieve the key tensor from parameters in the model
        value         = self.value      # Retrieve the value tensor from parameters in the model
 
        scaled_qk     = torch.nn.functional.scaled_dot_product(query, key) * scale_factor  # Apply dot product to query and key tensors, scale by a factor
        softmax_qk    = scaled_qk.softmax(dim=-1)                                                  # Apply softmax along the last dimension of the dot product
        dropout       = torch.nn.functional.dropout(
            softmax_qk, p=dropout_p)  # Apply dropout to the scaled dot product
        output        = torch.nn.functional.scaled_dot_product(
            dropout, value)  # Compute a new tensor by applying the scaled dot product of the dropout tensor and the value tensor
        
        return output


# Initializing the model
sa  = SelfAttention()
 
# Inputs to the model
q1, k1, v1 = torch.randn(32, 512),   \
             torch.randn(8,   32, 512), \
             torch.randn(8, 32, 512)
 
 
