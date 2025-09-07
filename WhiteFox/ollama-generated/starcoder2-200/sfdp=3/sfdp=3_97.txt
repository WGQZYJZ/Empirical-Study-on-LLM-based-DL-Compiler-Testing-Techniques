
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = torch.nn.Parameter(torch.rand([1, 1]))
        self.scale.requires_grad_()

        self.key_norm = torch.nn.LayerNorm([32 * 64]) # Normalize each channel in the key tensor with a learnable affine transform
        self.value_norm = torch.nn.LayerNorm(7) # Normalize each channel in the value tensor with a fixed transform

    def forward(self, query):
        self.key = self.key_norm(torch.rand([128 * 32, 64])) 
        self.dropout_p = np.random.uniform() 

        k = self.key
        v = torch.randn([7, 50])

        q = query
        scaled_qk = torch.matmul(q, k.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk *= scale 
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p) # Apply dropout to the softmax output

        output = dropout_qk.matmul(v).div(dropout_qk.sum()) # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing model
m = Model()

# Input to the model
query  = torch.randn([128, 3])
__output__  = m(query)

