
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_layer  = torch.nn.Linear(16, 32)

    def forward(self, qk):
        q  = qk[:,0,:,:] # Get the query vector from the first dimension of the query and key tensor
        k  = qk[:,1,:,:] # Get the key vector from the second dimension of the query and key tensor
        attn_mask = qk[:,:,2:3] * -math.inf

        v = self.attn_layer(qk)

        v = torch.transpose(v, 0, 1).contiguous() # Make it contiguous in memory so we can use batched matrix multiplication with @

        return torch.matmul(v, k)


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(2, 4, 32, 64) # x1: (2, 8, 32, 64), x2: (4, 8, 32, 64)
