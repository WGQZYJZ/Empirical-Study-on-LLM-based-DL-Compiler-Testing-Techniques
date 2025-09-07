
class Model(torch.nn.Module):
    def __init__(self, embedding_dim, hidden_size, num_heads=8, dropout_p=0.1):
        super().__init__()
 
        # Construct and initialize the encoder
        self.embedding = torch.nn.Embedding(vocab_size, embedding_dim)
        self.transformer_encoder = TransformerEncoder(embedding_dim, 
                                                     hidden_size, 
                                                     num_heads,
                                                     dropout_p)
 
        # Construct and initialize the decoder with a position-wise Feed-Forward layer on top
        self.layer = torch.nn.Linear(embedding_dim + hidden_size, embedding_dim)

    def forward(self, inputs, lengths):
        # Get the input mask
        input_mask = torch.zeros((inputs.shape[0], inputs.shape[1] - 1), dtype=torch.bool)
        input_mask[:, 1:] = True
 
        # Calculate the length of the sequence and calculate the length normalization value (LN)
        seq_len, _ = lengths.data.max(dim=1)
        ln = torch.mean(seq_len).unsqueeze(-1)
 
        # Pre-calculate some quantities we need for computing the weights and the biases
        # of the softmax distribution
        alpha_q = self.embedding.weight / ln

        # Construct the input mask
        bsz = inputs.shape[0]
        seq_mask = torch.triu(torch.ones((bsz, bsz), device=inputs.device))
        mask = (seq_mask < (1 - (input_mask[:, 1:] * input_mask[:, :-1]))) + 1
 
        # Reshape and batch vectorize the inputs to match what's in the batch of input_data.
        embeds = self.embedding(inputs)
        embeds = embeds.reshape((-1, embeds.shape[2]))
        embeds *= mask

        # Run a forward pass through the encoder. This is the same as applying the previous layer on top
        # of embeds before passing them to the hidden state in this layer.
        src_mask = seq_mask * input_mask[:, :-1]  # Get just the source mask, ignoring the time dimension.
        enc_out, _ = self.transformer_encoder(embeds, src_mask)

        # Calculate and return the weights (logits). This is done by calculating the dot product of
        # enc_out and value. For each element in the query tensor we compute the dot product with all elements
        # in the key tensor multiplied by alpha_q and sum them up. These are then normalized by LN.
        weighted_q = enc_out @ alpha_q
 
        # Get the hidden states of the last token, reshape to (batch size x hidden size)
        h = enc_out.reshape((-1, self.hidden_size))

        # Reshape to original batch shape and convert back into the 2D representation using a linear layer.
        v = torch.cat((h.contiguous().view(bsz, -1),
                        self.layer(torch.cat((weighted_q, embeds.contiguous().view(bsz, -1)), dim=1))),
                       dim=-1)
 
        # Calculate the log of the values in this batch. For each element in the logits tensor we compute
        # the logarithm of the value at that position and sum them up.
        log_probs = torch.nn.functional.log_softmax(v, dim=1)

        # Reshape to original batch shape and convert back into the 2D representation using a linear layer.
        v = torch.cat((h.contiguous().view(bsz, -1),
                        self.layer(torch.cat((log_probs, embeds.contiguous().view(bsz, -1)), dim=1))),
                       dim=-1)
 
        return v


# Initializing the model
m  = Model()


