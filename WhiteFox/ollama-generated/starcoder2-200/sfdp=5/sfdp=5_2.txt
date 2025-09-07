
class SelfAttention(torch.nn.Module):
    def __init__(self, in_channel: int) -> None:
        super().__init__()
 
        # Attention mask
        self._attn = torch.zeros(32, 512 * 7 * 7 + 160).fill_(float('-inf'))  # The attention mask is a vector of 49152 elements. This means there are 80 positions on average that the model should attend to.
        self._attn[ :, :32] = 0
 
        # Weight matrix for query, key and value
        self._in_qkv = torch.nn.Parameter(torch.empty((49152, in_channel)))
 
        # Initialization of the weight matrix
        torch.nn.init.normal_(self._in_qkv)
 
    def forward(self, inputs):
        batch_size  = inputs.shape[0] // 32  # The batch size is equal to 7 x 7 x 16 for each sample
 
        # Get query, key and value from the input tensor
        in1x1 = torch.chunk(inputs, 32)  # Chunking the input into 49152 parts of size 32 (for every position of the self-attention matrix), resulting in an array with 7 * 7 * 16 positions
 
        q_ = []
        k_ = []
        v_ = []
        for b in range(batch_size):
            a1x1, a2x1, a3x1 = torch.chunk(in1x1[b], 4) # Chunking each sample into 7 parts of size 7 (for every row), resulting in an array with 16 positions
 
            # Compute query from 4 chunks of the 16 channels for each row, concatenating them together along the batch dimension.
            q_ = torch.cat([self._in_qkv @ a1x1[:, None], self._in_qkv @ a2x1[:, None],
                self._in_qkv @ a3x1[:, None]], dim=0)
 
            # Compute key from 4 chunks of the 16 channels for each row, concatenating them together along the batch dimension.
            k_ = torch.cat([self._in_qkv @ a1x1[:, None], self._in_qkv @ a2x1[:, None],
                self._in_qkv @ a3x1[:, None]], dim=0)
 
            # Compute value from 4 chunks of the 16 channels for each row, concatenating them together along the batch dimension.
            v_ = torch.cat([a1x1, a2x1, a3x1], dim=0)
 
        # Apply dot-product attention
        o = torch.bmm(q_.unsqueeze(dim=-2), k_.permute(-1, -2).contiguous()) / math.sqrt(q_.size(-1)) + self._attn[:, None]  # Compute the dot product of the query and key, then scale it by dividing by the square root of the number of channels in the batch
        o = F.softmax(o, dim=-1)
 
        # Apply dropout to attention weights, and apply it to the value
        o = torch.dropout(o, 0.2, True)
        out = self._in_qkv @ v_.permute(-1, -3).contiguous()
        return o

