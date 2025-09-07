
class Model(torch.nn.Module):
    def __init__(self, d_model=512, dropout=0.1):
        super().__init__()

        # Keys and queries have dimension d_model=512 (768 if batched)
        self.key = torch.nn.Linear(d_model, d_model, bias=False)
        self.query = torch.nn.Linear(d_model, d_model, bias=False)

        # Value is 3D so apply dimension reduction for each axis
        self.value = torch.nn.Linear(d_model, 1)
        self.attn_drop = torch.nn.Dropout(dropout).to("cuda")

    def forward(self, x):
        # Compute scaled dot product of keys and queries to get attention weights wk and wq
        # Scale the dot products by the square root of d_model (512) - this is due to some theoretical reasons. In a future implementation we will have an option that will not do this
        scale = x.shape[-1] ** -0.5

        # Compute scaled dot product of keys and queries as the element wise multiplication of two tensors of shape [b, d_model], divided by its square root (in place on GPU)
        # This will compute wq @ k.transpose(-2, -1). For better memory usage, use a batch matrix multiply
        q = self.query(x).float() * scale
        k = self.key(x).float().transpose(-2, -1)

        # Add the attention mask
        k += attn_mask[..., None]

        # Compute the softmax and dropout to get the attention weights
        attn_weight = torch.softmax(k @ q, dim=-1)
        attn_weight = self.attn_drop(attn_weight).to("cuda")

        # Multiply by the value to get the output of this layer in the feed forward model (without a bias) and return it
        return x + 0.5 * ((self.value(x)).float() @ torch.softmax(attn_weight, dim=-1))


# Initializing the model
model = Model().cuda()

 # Inputs to the model. The input here is 3D, but for better memory usage it would be 2D - in that case the batch matrix multiply (AK) would be used instead of matmul. For GPU you could also use a batched implementation without using a torch.matmul. 
 x = torch.randn(4, 8, 768).cuda()

# The expected output from this model:
