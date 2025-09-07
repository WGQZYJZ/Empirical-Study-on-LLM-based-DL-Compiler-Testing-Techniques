
class Model(torch.nn.Module):
    def __init__(self, config):
        super().__init__()

        # Create a single linear layer that converts a key into a dense vector.
        self.key = torch.nn.Linear(config['model_dim'], 128)

    def forward(self, query, value, keys=None, query_length=None, key_padding_mask=None):
        # Get the shape of the current batch to generate attention mask if needed later
        batch_size = input_ids.shape[0]

        # Concatenate the `query` and `value` tensor for the linear layer in this module.
        x = torch.cat((query, value), dim=1)  # (batch_size * seq_len, hidden_dim*2)
        # Reshape and permute to generate the key input that is used by the linear layer.
        x = x.reshape(batch_size * query_length, -1).permute(0, 2, 1)
        # Generate attention mask based on `key_padding_mask` if it exists
        attn_mask = torch.unsqueeze(torch.arange(0, batch_size), dim=1) < torch.unsqueeze(query_lengths, dim=0)

        if key_padding_mask is not None:
            # Concatenate the `query`, `value` and `key_padding_mask` tensor for the linear layer in this module.
            x = torch.cat((x, key_padding_mask), dim=1)  # (batch_size * seq_len, hidden_dim*2+attn_mask_dim)
        # Reshape to generate input tensor of size `[seq_len, batch_size*hidden_dim]`. The `1` in the shape is used for broadcasting.
        key = self.key(x).reshape(-1, query_length, self.config['model_dim'])

        if keys is not None:
            # Generate attention score matrix based on all-keys
            attn = torch.einsum('bijd,bdj->bijd', (query, keys)).div_(attn_mask.type(attn_mask.dtype).expand(attn_mask.shape))
            key = torch.cat((key, attn), dim=-1)  # (batch_size * seq_len, hidden_dim*2+attn_mask_dim, query_num)

        if key is not None:
            # Compute the scaled dot product of `query` and each key in `keys`.
            attn = torch.einsum('bijd,bdjk->bijk', (query, key))
            attn = attn.softmax(dim=-1)

            # Masked softmax with `dropout_p` probability
            if self.training:
                # Apply dropout to the scaled dot product of the query and each key in `keys`. The result will be a tensor that contains the probabilities of applying attention on each value based on its current location in sequence. After multiplying by the inverse temperature, the softmax function takes an unnormalized probability distribution as input, then produces a normalized probability distribution as output.
                attn = torch.nn.functional.dropout(attn, p=self.config['attention_dropout_p'])
            # Apply attention mask to each value based on its current location in sequence.
            attn = attn * attn_mask

            key = torch.einsum('bijk,bdjk->bijd', (attn, keys))  # (batch_size * seq_len, hidden_dim*2+attn_mask_dim, query_num)
        else:
            key = attn

        if keys is not None:
            key = key[:, :, :query.shape[-1]]

        return query, key, attention


# Initializing the model
m = Model(config)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
