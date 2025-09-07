qk  = query @ key.transpose(-2,-1)/math.sqrt(query.size[-1]) # Apply a dot product to compute the similarity between query and key. Then, apply a sqrt normalization operation.
qk  = qk + attn_mask # Add the attention mask
attn_weight  = torch.softmax(qk, dim=-1)  # Compute the softmax of the similarity map. The attention weights are obtained as the softmax of the scaled dot product.
attn_weight  = torch.dropout(attn_weight, dropout_p=0.5, training=self._mode_training)  # Apply dropout to the attention weight with probability .5 (applied with probability .25 in each iteration for a total of three steps. If dropout is applied during inference, then .75 will be used.)
output       = attn_weight @ value  # Compute the dot product between attention weights and value vectors.
qk  = query @ key.transpose(-2,-1)/math.sqrt(query.size[-1]) # Apply a dot product to compute the similarity between query and key. Then, apply a sqrt normalization operation.
qk  = qk + attn_mask # Add the attention mask
attn_weight  = torch.softmax(qk, dim=-1)  # Compute the softmax of the similarity map. The attention weights are obtained as the softmax of the scaled dot product.
attn_weight  = torch.dropout(attn_weight, dropout_p=0.5, training=self._mode_training)  # Apply dropout to the attention weight with probability .5 (applied with probability .25 in each iteration for a total of three steps. If dropout is applied during inference, then .75 will be used.)
output       = attn_weight @ value  # Compute the dot product between attention weights and value vectors.
