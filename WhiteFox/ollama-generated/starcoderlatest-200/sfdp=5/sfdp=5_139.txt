
class Model(torch.nn.Module):
    def __init__(self, embedding_dim=16, num_heads=4, num_attention_layers=2):
        super().__init__()

        self.embedding = torch.nn.Embedding(256, embedding_dim)
        self.positional_encoding = torch.nn.Parameter(torch.randn(
            (32*8)*4+1,
            embedding_dim,
            dtype=torch.float))
 
        layers = []
        for _ in range(num_attention_layers):
            layers += [
                MultiheadAttentionLayer(
                    self.embedding.embedding_dim, 
                    num_heads=num_heads)
            ]

        self.decoder = torch.nn.Sequential(*layers)

    def forward(self, inputs, lengths=None):
        batch_size, seqlen, embed_dim = inputs.shape
        position_encoding = self.positional_encoding[:batch_size*seqlen] # Batch size * sequence length

        positional_encoding = torch.transpose(
            position_encoding, 0, -1)  # [B, E]
        positional_encoding = positional_encoding.unsqueeze(dim=0).repeat(
            32, 1, 1)  # [32, B, E]
        inputs += position_encoding

        x = self.embedding(inputs)

        # Attention Mask
        if lengths is not None:
            padded_sequence_lengths = torch.arange(
                1, seqlen + 1).view(seqlen + 1).repeat((batch_size, 1))

            padded_sequence_lengths[1:] += torch.cat([
                torch.tensor([0], dtype=torch.int), 
                padded_sequence_lengths[:-1] - padded_sequence_lengths[1:])
            assert (padded_sequence_lengths[1:-1].sum() == seqlen + 1).all(), "Padding error"
            max_len = padded_sequence_lengths[0, -1]
            attention_mask = torch.zeros(
                batch_size*max_len, max_len, dtype=torch.float32)

            for b in range(batch_size):
                start = padded_sequence_lengths[b, 0].item() - 1
                end = padded_sequence_lengths[b, seqlen+1]

                attention_mask[b, :end-start] = 1

            # (B, L, L)
            attention_mask = torch.transpose(
                attention_mask, 0, -1).unsqueeze(dim=2).repeat(
                    32, 1, 1)  # [32, B, L, L]

        x = self.decoder(x, None, attention_mask)
        return x


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 32, 64, 64)
