
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1):
        # Create tensors for query, key and value
        query = torch.randn((2, 3))
        key = torch.randn((2, 5))
        value = torch.randn((2, 4))
 
        # Compute the dot product of the query and key tensors
        dot_product = torch.matmul(query, key.transpose(-1, -2))
        
        # Create an inverse scale factor (to be added to the scaled dot product)
        inv_scale_factor = 5
        scaled_dot_product = dot_product + inv_scale_factor
 
        # Compute softmax of the scaled dot product
        softmaxed_dot_product = torch.softmax(scaled_dot_product, dim=-1)
 
        # Create dropout probability (to be used as a parameter to the dropout function)
        dropout_p = 0.3
        
        # Apply dropout with probability p
        dropout_masked_dot_product = torch.nn.functional.dropout(softmaxed_dot_product, p=dropout_p)
 
        # Compute dot product of dropout output and value tensor
        v_output = dropout_masked_dot_product @ value
 
        return v_output

# Initializing the model with input 1
input1  = torch.randn(200, 5384)

m  = Model()

__output__  = m(input1)

