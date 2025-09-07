
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = 1 / np.sqrt(16)
 
        # Initializing query, key and value tensors for the attention
        self._qkv = torch.nn.ParameterList() 
        self._qkv.append(torch.nn.Parameter(torch.randn(32, 54780)))
        self._qkv.append(torch.nn.Parameter(torch.randn(32, 196610)))
        self._qkv.append(torch.nn.Parameter(torch.randn(32, 32768)))
 
    def forward(self):
        v1 = torch.matmul(self._qkv[0], self._qkv[1].transpose(-2, -1)) # Compute the dot product of query tensor and key tensor for 1st part 
        v2 = self.scale * v1 # Scale the dot product by a factor
        v3 = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        v4 = torch.nn.functional.dropout(v3, p=0.5) # Apply dropout to the softmax output for 2nd part 
        v5 = v4.matmul(self._qkv[2]) # Compute the dot product of the dropout output and value tensor
        
        return (v1, v2, v3, v4, v5) # Return the three intermediate outputs

# Initializing the model
m  = Model()

