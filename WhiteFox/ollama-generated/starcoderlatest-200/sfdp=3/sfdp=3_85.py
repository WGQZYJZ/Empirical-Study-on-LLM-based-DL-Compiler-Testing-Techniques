
class Attention(torch.nn.Module):
    def __init__(self, hidden_size, num_attention_heads):
        super().__init__()
        self.num_attention_heads = num_attention_heads
        self.attention_head_dim = hidden_size // num_attention_heads

        self.query = torch.nn.Linear(hidden_size, hidden_size)
        self.key   = torch.nn.Linear(hidden_size, hidden_size)
        self.value = torch.nn.Linear(hidden_size, hidden_size)
 
        self.dropout = torch.nn.Dropout(p=attention_dropout_p)
 
    def transpose_for_scores(self, x):
        new_x_shape = x.size()[:-1] + (self.num_attention_heads, self.attention_head_dim)
        x = x.view(*new_x_shape)
        return x.permute(0, 2, 1, 3)
 
    def forward(self, attention_mask=None, head_mask=None, inputs_embeds=None, encoder_hidden_states=None, encoder_attention_mask=None):
        mixed_query_layer = self.query(inputs_embeds) 
        # Apply a linear projection to the hidden state features of the last layer
        query_layer      = mixed_query_layer + attention_mask 

        key_layer   = self.transpose_for_scores(self.key(encoder_hidden_states))  
        # Transpose the last two dimensions

        value_layer = self.transpose_for_scores(self.value(encoder_hidden_states)) 
        # Transpose the last two dimensions

        query_layer = self.dropout(query_layer) 
        
        key_layer   = self.dropout(key_layer) 

        attention_scores = torch.matmul(query_layer, key_layer.transpose(-2, -1)) 
        attention_scores /= math.sqrt(self.attention_head_dim)
        # Take the dot product between "query" and "key" to get the raw attention scores

        if self.dropout_p != 0.0:
            attention_scores = self.dropout(attention_scores) 

        # Apply the attention mask is (precomputed for all layers in BertModel forward() function)
        if attention_mask is not None:
            # Apply the attention mask is (precomputed for all layers in BertModel forward() function)
            attention_scores = attention_scores + attention_mask 

        # Normalize the attention scores to probabilities. Add a small constant for numerical stability 
        attention_probs = torch.nn.Softmax(dim=-1)(attention_scores) 
        # Apply softmax to the raw attention scores.

        attention_probs = self.dropout(attention_probs) 


        if head_mask is not None:
            attention_probs = attention_probs * head_mask 

        context_layer = torch.matmul(attention_probs, value_layer)
        # Take the dot product between "attention_probs" and "value" to get the context vector

        context_layer = context_layer.permute(0, 2, 1, 3).contiguous()  
        new_context_layer_shape = context_layer.size()[:-2] + (self.num_attention_heads * self.attention_head_dim)
        # Final shape: batch_size x max_position_embeddings x sum_of_attention_heads x attention_head_dim

        context_layer = context_layer.view(*new_context_layer_shape)  
        # Transpose to be flat, rearrange the dimensions
        mixed_context_layer  = self.dropout(context_layer) 
        # Final shape: batch_size x sum_of_attention_heads x max_position_embeddings x attention_head_dim
 
        output = mixed_query_layer + mixed_context_layer 

        return output


class TransformerModel(torch.nn.Module):
    def __init__(self, config):
        super().__init__() 
        self.config = config

        self.embedding     = torch.nn.Embedding(config.vocab_size, config.hidden_size)
        # Load the embedding matrix for the vocabulary of GPT2-based models

        self.transformer   = AttentionModel(config) 
        # A transformer model

    def forward(self, input_ids=None, attention_mask=None): 
        if input_ids is not None:
            # Inputs are in shape [batch_size x seq_length]
        # We need to flatten the first dimension into a list of integers

        attention_mask = self._create_attention_mask(input_ids)  
        # Create an attention mask

        embedding_output = self.embedding(input_ids) 
        # The embedding layer is pre-trained on a large corpus and therefore performs better than the untrained layer

        encoder_hidden_states  = torch.nn.LayerNorm(self.config.hidden_size, eps=1e-6)(embedding_output + attention_mask)  
        # The output of the embedding layer plus the attention mask are used to compute a new embedding vector for each token in the input sequence

        outputs               = self.transformer(attention_mask=attention_mask, head_mask=None, inputs_embeds=encoder_hidden_states) 
        # Apply a transformer model that is pre-trained on GPT2 and performs very well
 
        return outputs

    def _create_attention_mask(self, input_ids):  
        attention_mask = torch.zeros_like(input_ids)
        for i in range(1, self.config.max_position_embeddings + 1):  
            #
        if len(x_squad_):
            x = self._encoder(").join(list(map(str, x_s))))
def test_model():
  