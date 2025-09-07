
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_k = torch.nn.Linear(1024, 512)
        self.linear_q = torch.nn.Linear(1024, 512)
        self.linear_v = torch.nn.Linear(1024, 512)
 
    def forward(self, q1, v1):
        k1 = torch.nn.functional.adaptive_avg_pool2d(q1, (64, 64)) # Reduce the query tensor to size (1, 512, 64, 64)
        k1 = self.linear_k(k1.reshape(-1, 512)).view(-1, 3, 64, 64).permute(0, 2, 3, 1) # Apply linear transformation to get the new key tensor 
        q1 = torch.nn.functional.adaptive_avg_pool2d(q1, (64, 64)) # Reduce the query tensor to size (1, 512, 64, 64)
        q1 = self.linear_q(q1.reshape(-1, 512)).view(-1, 3, 64, 64).permute(0, 2, 3, 1) # Apply linear transformation to get the new query tensor 
        v1 = torch.nn.functional.adaptive_avg_pool2d(v1, (64, 64)) # Reduce the value tensor to size (1, 512, 64, 64)
        v1 = self.linear_v(v1.reshape(-1, 512)).view(-1, 3, 64, 64).permute(0, 2, 3, 1) # Apply linear transformation to get the new value tensor 
        qk = torch.matmul(q1, k1.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(scale_factor) # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(v1) # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()

# Inputs to the model
q1 = torch.randn(1, 3, 64, 64)
v1 = torch.randn(1, 3, 64, 64)
