
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.functional.linear  # Use a public API to compute the dot product, which is an attention operation in transformer model
        self.softmax = torch.nn.Softmax()   # Use a public API to apply softmax
        self.dropout = torch.nn.Dropout(p=0.1)
 
    def forward(self, query):
        key = torch.randn(256, 256) * 1e-3  # Initialize the key tensor with random numbers multiplied by a small constant
        value = torch.randn(256, 4) * 0.07  # Initialize the value tensor with random numbers multiplied by a small constant

        # Inputs to the model
        inv_scale_factor  = 1e-3   # Initialize the inverse scale factor
 
        query *= inv_scale_factor 
        vqk = self.matmul(query, key)
        scaled_qk = vqk.div_(inv_scale_factor)

        softmax_qk = scaled_qk.softmax(dim=-1)  
        v1  = self.dropout(softmax_qk)  
        output  = v1.matmul(value)  
        return output


# Initializing the model
m  = Model()
 
query = torch.randn(32, 480).repeat((16,)) * inv_scale_factor

