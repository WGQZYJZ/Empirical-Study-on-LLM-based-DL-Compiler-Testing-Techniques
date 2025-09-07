class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(64, 128) # Initialize the query linear layer with weight matrix of size 64x128 and bias vector of size 128, using Xavier uniform initialization
        self.key_value = torch.nn.Linear(3 * 1024, 512)
 
    def forward(self, qkv):
        q = self.query(qkv) # Apply the query linear layer to the input tensor qkv
        k, v = torch.chunk(self.key_value(qkv), chunks=[64], dim=0) # Divide the result of the key value linear layer into two parts: k and v
        k = k * math.sqrt(query.size(-1))  # Scale the dot product of q and k by a sqrt constant to prevent their explosion or disappearance during softmax operation
        qk  = torch.bmm(q, k.transpose(0, 1).contiguous())  # Compute the dot product between the query tensor and key transpose tensor
        mask_value = -1e9  # Set the value for masked elements in the attention weight calculation to -1e9
        attn_mask = torch.ones((qkv.size(-2), qkv.size(-2)), device=qk.device, dtype=qk.dtype) + mask_value * (1-attn_mask).float()  # Create an attention mask that sets the diagonal elements to -1e9 and other elements are set as 0
        attn_weight = torch.softmax(q, dim=-1) @ mask_value # Compute the softmax of the dot product of q and the result of matrix multiplication
        output = torch.bmm(attn_weight, v)  # Compute the dot product between the weight tensor obtained from the softmax operation on the query tensor and value tensor
        return output
torch.nn.Linear: 64, 128
qk: (1, 64) torch.Size([batchsize x sequence length x embedding_dimension * 3])
