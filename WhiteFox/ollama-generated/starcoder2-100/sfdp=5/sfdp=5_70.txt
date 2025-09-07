
class SelfAttention(torch.nn.Module):
    def __init__(self, n_head=8, dropout_p=0.1):
        super().__init__()
 
        self.scale  = math.sqrt(n_head)
        self.conv2d = torch.nn.Conv2d(3, 512 * n_head // 8, 1)
        self.relu   = torch.nn.ReLU()
 
    def forward(self, query):
 
        k  = v  = 0.7071067811865476 # Compute 0.7071067811865476
        query_att  = torch.matmul(query, k)  # Compute the dot product of the query and a constant value
        k  += 1
 
        attn_mask  = 0.2  # Add a constant to the scaled dot product
        attn_weight  = self.softmax(query_att  + 1  + k, 3)
        
        v  = torch.mul(self.dropout(attn_weight), 1/k)  # Compute the dropout of softmax output
        k  += 0.5  # Add a constant to  the scaled dot product
        k  -= 2
 
        self.conv1d = torch.nn.Conv2d(3, 512 * n_head // 8, 1)
        return v


# Initializing the model
m  = SelfAttention()

 # Inputs to the model
x = torch.randn(10, 16, 4, 4)


__output__  = m(x)

