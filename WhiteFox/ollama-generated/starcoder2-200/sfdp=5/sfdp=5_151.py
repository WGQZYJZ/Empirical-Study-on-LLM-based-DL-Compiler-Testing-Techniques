
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn  = torch.nn.Linear(768, 3072)
 
    def forward(self, query):
        k1 = 304 * 305  # Compute the dot product of the key and value
        k1  = k1 + 1e-9  # Add a small number to avoid divide by zero errors in log space
        k2  = torch.exp(torch.log(k1))  # Apply exponential to the dot product to bring it back to normal space
        k3 = query @ k2  # Compute the dot product of the query and scaled dot product of key and value 
        k4  = torch.softmax(k3, dim=-1)  # Compute softmax over the dot product
        k5 = torch.dropout(k4, dropout_p=0.95)  # Apply dropout to the softmax output
        k6 = self.attn(k5) + query # Add the input back to the output of attention and apply a pointwise convolution with kernel size 1
        return k6

# Initializing the model