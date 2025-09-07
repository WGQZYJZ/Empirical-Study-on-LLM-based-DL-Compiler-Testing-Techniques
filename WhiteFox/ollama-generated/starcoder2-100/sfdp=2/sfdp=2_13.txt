
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Linear(768, 3 * 512)
 
    def forward(self, x):
        qkv_out  = self.qkv(x).chunk(3, dim=1) # Split the output of the Linear layer into three parts, where each part is the size of [B, 768]
        v, k, q  = tuple([torch.nn.functional.normalize(x_k) for x_k in qkv_out])
        k_expand = k.view(*q.shape[:-1], -1).transpose(-2, -1) # View the key tensor so that the last two dimensions are [B * head_dim, head_dim]
        scaled_qk  = torch.matmul(q, k_expand) / (768**0.5)# Compute the dot product of the query and the key
        scaled_qk  = scaled_qk.div_(491.)# Scale the dot product by a fixed scale factor
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1) # Apply softmax to the scaled dot product 
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=0., training=self._training) # Apply dropout to the softmax output
        output  = dropout_qk.matmul(v) # Compute the dot product of the dropout output and the value tensor 
        return output

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(8, 768).chunk(3)[2]
__output__  = m(x1)

