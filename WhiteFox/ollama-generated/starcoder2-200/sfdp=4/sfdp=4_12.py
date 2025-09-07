class TransformerModel(torch.nn.Module):
    def __init__(self) -> None:
        super().__init__()

        # This is the embedding matrix that takes input token indices and converts them into vectors of fixed size.
        self.encoder = torch.nn.Embedding(vocab_size, embed_dim)
        
        # Here we construct the two multi-head attention layers.
        self.pos_encoder1 = PositionalEncoding(embed_dim) 
        self.att1 = MultiHeadedAttention(h=num_heads, d_model=embed_dim)

        # This is a linear layer that maps from the encoded input sequence to a vector of dimension `d_out`.
        self.pos_encoder2 = PositionalEncoding(d_model) 
        self.att2 = MultiHeadedAttention(h=num_heads, d_model=embed_dim) 

        # This is the linear layer that takes the result of the encoder/decoder attention block and converts it into a sequence with the same length as the original input (the length of the output sequence).
        self.output = torch.nn.Linear(d_model, vocab_size)

    def forward(self, inputs):
        
        # The input `inputs` is an index sequence that contains token indices.
        # We will call it a "sequence" because we want to view it as a 3D tensor of shape (batch size x seq length x dimension). 
        inputs = inputs.permute(1,0)  

        batch_size = inputs.shape[1]

        # To be able to use the model for inference at test time, we need to provide two kinds of input:
        # 1. a sequence that contains indices. This is what we call `inputs`. 
        # 2. A `memory` tensor which was obtained by passing in the sequence twice (one time forwards and one backward).

        # Here we will concatenate both the forward and backward representation to form the memory tensor.
        # However, for the first batch of the training set, there are no backwards embeddings that we can compute yet. 
        # Therefore, in the first batch `inputs_with_forward` will be a 2D tensor with shape (batch size x seq length). 
        # When we later compute `memory`, we will have the backwards representations and concatenate them. 
        inputs = torch.cat([inputs, self.encoder(inputs)], dim=1) 

        # Now we call `PositionalEncoding` which adds positional encoding to the embedded sequence
        outputs = self.pos_encoder2(self.att2(self.att1(self.pos_encoder1(inputs),inputs), inputs))
        
        # Now we call a linear layer that takes as input our attention block output (the encoder/decoder output) 
        # and maps it to the vocabulary size.
        return self.output(outputs).permute(1,0)
