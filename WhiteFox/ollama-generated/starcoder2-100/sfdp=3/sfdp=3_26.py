
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1, k1, v1):
        scale  =  0.7071067811865476 
        drop_p =   0.3 # Probability to perform dropout
 
        v2 = torch.nn.functional.dropout(q1.mul(k1.transpose(-2, -1)).softmax(dim=-1), p=drop_p)
        v3  =   v2.matmul(v1) 
        
        return v3


# Initializing the model
m  = Model()
# Input tensors to the model
v1 = torch.randn(16,   4,    70,     50) # value tensor of shape [batch_size x head_num x seq_len x head_dim]
v2 = v1.transpose(-3,-2)  # Reshape the value tensor to be [batch_size x head_num x head_dim x seq_len]
k1 = torch.randn(16,   4 ,70,      50) # key tensor of shape [batch_size x head_num x head_dim x query_seq_len] 
q1 = v1 @ v2 # Compute the dot product between the value and key tensors
 
