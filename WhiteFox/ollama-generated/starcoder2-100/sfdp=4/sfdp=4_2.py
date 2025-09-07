
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.attn = torch.nn.Linear(embed_dim, embed_dim)
 
    def forward(self, query, key, value):
        # Calculate scaled dot-product attention
        scale  = key.size(-1)**(-0.5)
        scaled_attn  = query @ key.transpose(-2, -1)*scale
        scaled_attn += self._mask() 
        scaled_attn = torch.softmax(scaled_attn, dim=-1)
 
        # Compute the dot product of attention weights and value
        attn_output  = scaled_attn @ value
        return attn_output
 
    def _mask(self):
        # Create a triangular mask that is applied to each row (i.e., the length of the sequence we want to attend over) 
        #  using `tril` function
        n  = self._query.size(-2) # Number of sequence elements,  = self._query.size(1) or batch_size * sequence_len
        mask = torch.ones([n + i for i in range(n)])
        mask = mask.tril() 
        # Create a triangular matrix that is used to create the attention mask.
        mask.add_(mask < 2, value=float("-inf"))
 
        return mask
 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.embed = torch.nn.Embedding(vocab_size, embed_dim)
        self.position_encoding = PositionalEncoding(embed_dim)
        self.attn  = Attention()
 
    def forward(self, inputs):
         # Embed the inputs
         inputs = self.embed(inputs)
 
         # Create an attention mask for padding tokens
         input_mask  = inputs == self._padding_idx
         
         # Calculate positional encodings based on word position in the sequence
         position  = torch.arange(inputs.size(-1), dtype=torch.int64, device=inputs.device)
         posi_emb  = self.position_encoding(position).permute([0,2,1])
 
         # Add positional encodings to embedded inputs and then apply the attention layer 
         attn  = self.attn(inputs+posi_emb, inputs+posi_emb, inputs)
         
        return attn

m  = Model()


# Inputs to the model (batch size of 2; sequence length: [8] for 1st input tensor and [7]; 6 for the second one.)
input  = torch.nn.functional.one_hot(torch.tensor([0,4]), vocab_size).to(torch.int32)
input  = torch.cat([input]*2, dim=0) # Batch size is 1* 2* 8
input[1][7]  = -9  # Pad the last element of the second input to be -9 (i.e., set to the value 3 which is outside of the vocabulary)

