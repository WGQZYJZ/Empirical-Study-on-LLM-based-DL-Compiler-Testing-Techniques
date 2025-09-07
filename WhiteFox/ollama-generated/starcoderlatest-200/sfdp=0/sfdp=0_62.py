This pattern characterizes the Scaled Dot-Product Attention mechanism, which is a key component of Transformer models. In this mechanism, the attention weights are computed as the softmax of the scaled dot product of the query and key tensors. These weights are then used to compute a weighted sum of the value tensor. The scaling factor `inv_scale` is typically the square root of the dimension of the key/query vectors, which helps to stabilize the gradients especially when the dimensions are large.


# Description of requirements
The model should contain the following pattern:
This pattern characterizes attention mechanisms in Transformer models where `q` and `k` share a single head (i.e., dim) as suggested by the original transformer paper, but different keys or values might be assigned to different heads. Also note that d_k should match the dimension of the final layer before softmax to generate the scaled attention weights.

# Model
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, head_dim):
        super().__init__()
        self.head_dim = head_dim
        self.qkv = torch.nn.Linear(64, 2*3*head_dim)
 
    def forward(self, qkv):
        bs, d, h = *qkv.shape, -1
        assert d % (3*h) == 0 and 64 % h == 0
 
        kv = qkv.reshape(bs,3,-1,h).permute(0,2,1,3).reshape(bs,-1,h) # (batch,3,512,8)
        assert kv.shape[1] >= self.head_dim, 'Invalid heads dimension, it should be greater than or equal to number of head dimensions'
 
        q = kv[:,:self.head_dim].transpose(-2,-1).reshape(bs, 3, -1) # (batch,3,64) -> (batch,3,8)
        k = kv[:,self.head_dim:2*self.head_dim].transpose(-2,-1).reshape(bs, 3, -1) # (batch,3,64) -> (batch,3,8)
        v = kv[:,2*self.head_dim:].transpose(-2,-1).reshape(bs, 3, -1) # (batch,3,64) -> (batch,3,8)
 
        qk = torch.matmul(q, k.
