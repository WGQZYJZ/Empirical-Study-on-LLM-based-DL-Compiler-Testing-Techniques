
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(256 * 64 * 64, 256) # The first fully-connected layer
        self.linear2 = torch.nn.Linear(256, 3072) # The second fully-connected layer
        self.linear3 = torch.nn.Linear(3072, 768 * 8 * 8) # The third fully-connected layer

    def forward(self, x):
        v1 = self.conv(x) # Apply convolution with kernel size 1 to the input tensor
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        x_ = self.linear(v6) # Apply linear transformation to the output of the convolution
        return x_, attention_weights

class SelfAttentionWithScaledDotProductAttention(nn.Module):
    def __init__(self, dim=768, num_heads=12):
        super().__init__()
        self.num_heads = num_heads

        # key, query, and value: 256 x 3072 tensor
        self.linear_keys = torch.nn.Linear(dim * 3, dim)
        self.linear_queries = torch.nn.Linear(dim * 3, dim)
        self.linear_values = torch.nn.Linear(dim * 3, dim)

        # Weights: 256 x 3072 x 12 tensor
        self.linear_keys_weights = torch.nn.Linear(dim * 3, num_heads * dim)
        self.linear_queries_weights = torch.nn.Linear(dim * 3, num_heads * dim)
        self.linear_values_weights = torch.nn.Linear(dim * 3, num_heads * dim)

        # Outer product matrix: 256 x 12 tensor
        self.linear_attention_scores = torch.nn.Linear(num_heads * dim, dim)

    def forward(self, x):
        # The shape of x is batch_size x input_sequence_length x seq_length x embedding_dim

        scaled_dot_product_keys = self._scaled_dot_product_attention(x, self.linear_keys,
                                                                         self.linear_keys_weights)
        scaled_dot_product_queries = self._scaled_dot_product_attention(x, self.linear_queries,
                                                                           self.linear_queries_weights)

        attention_weights_values = self._scaled_dot_product_attention(scaled_dot_product_queries,
                                                                         scaled_dot_product_keys,
                                                                         self.linear_values,
                                                                         self.linear_values_weights)

        attention_scores = torch.matmul(attention_weights_values,
                                        torch.transpose(self.linear_attention_scores(
                                            attention_weights_values), 1, 2))
        scaled_attention_scores = F.softmax(attention_scores.unsqueeze(-1), dim=-1)

        return self._apply_scaled_attention(x, scaled_attention_scores, scaled_dot_product_queries,
                                              scaled_dot_product_keys)

    def _scaled_dot_product_attention(self, query, key, value, attention_weights):
        batch_size = query.shape[0]
        seq_length = query.shape[2]

        # Linearly project the query and the key to get q and k, respectively. Note that here we will not learn an additional projection layer for queries since queries are fixed in all time steps
        query_key = torch.cat((torch.matmul(query, self.linear_queries).view(-1, seq_length,
                                                                               self.num_heads * 3),
                                torch.matmul(key, self.linear_keys).view(-1, seq_length,
                                                                             self.num_heads * 3)), dim=-1)
        # Linearly project the value to get v
        query_value = torch.matmul(value, self.linear_values).view(-1, seq_length, self.num_heads * 3)

        scaled_dot_product_attention_weights = F.softmax(self.linear_attention_scores(query_key), dim=-1)

        attention_output = torch.matmul(scaled_dot_product_attention_weights, query_value).view(
            -1, self.num_heads * 3, seq_length)
        # Note: this output shape is batch_size x 3072 x seq_length since we have split the keys/values into 2 parts to do two separate attention operations (with different weights), then concatenated at the last dimension to compute an overall attention score for each head

        # Compute the context vector, apply dropout and linear transformation
        attention_output = F.dropout(attention_output, self.training)
        attention_context_vector = torch.matmul(attention_output,
                                                 torch.transpose(self.linear_attention_scores(query_key), 1,
                                                                 2)).view(-1, seq_length,
                                                                                3072 * 4)

        # Compute the output of each head
        attention_weights += self._apply_scaled_attention(x, scaled_dot_product_attention_weights, query_key,
                                                          attention_context_vector)

        return attention_weights

    def _apply_scaled_attention(self, x, scaled_dot_product_c)
    #     self.loss = = = = =
        self.accuracya = nn.BCELoss(
        )
        if (not args['enable_self_attention':False]).lower() == "true":
            loss = loss + torch.sum(self.self_attentionattentionattentionattention())

        if (self.use_bert is not None) and (not self.freeze):
            pooled_output, _ = self.model_for_output_layer(self.input_ids.transpose(0, 1).long(),
                                                            
                                                                   attention mask=None, 
                                                                   output_all_encoded_layers = True,)
        
        if not args.use_gpu or torch.cuda.is_available():
            pooled_output = pooled_output.detach().cpu()
        else:
            pooled_output = pooled_output.detach().cpu()

        return self._activation_function(pooled_output)
