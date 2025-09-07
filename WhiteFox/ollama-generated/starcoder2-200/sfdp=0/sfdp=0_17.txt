
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, config):
        super().__init__()
 
    def forward(self, query, key, value, attention_mask=None, output_attentions=False):
 
        batch_size  = query.shape[0] # 1 for batch size 1
        seq_len     = query.shape[-2] # 64 for query sequence length of 64
        dim         = query.shape[-1] # 384 for dimensionality of query, key, and value
 
         <|>  self.inv_scale  = torch.tensor(math.sqrt(dim)) 
 
         if attention_mask is not None:
            attention_mask = attention_mask == -float('inf')  # mask is a ByteTensor
        attention_weights = torch.matmul(query, key.transpose(-2, -1) / self.inv_scale)
        attention_weights = attention_weights * ~attention_mask
 
         if not output_attentions:
            attention_weights  = attention_weights.softmax(dim=-1)
 
         if self.training or not output_attentions and not self.output_all_encoded_layers:
             return attention_weights
 
          <|>  self._attn_output     = attention_weights .matmul(value)
 
         elif self.training or (not self.output_hidden_states and not self.output_all_encoded_layers):
             return attention_weights, self._attn_output
 
         return attention_weights, self._attn_output, value


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        config = BertConfig()
 
        self.bert           = BertModel(config)  # call BERT
        self.layer          = ScaledDotProductAttention(config)
 
    def forward(self, input_ids=None, attention_mask=None, output_attentions=False):
 
        outputs             = self.bert(input_ids, attention_mask, output_attentions)
 
        output              = self.layer(outputs['last_hidden_state'], outputs['last_hidden_state'], outputs['last_hidden_state'])
        return output


# Initializing the model 
m     = Model()
 
input1           = torch.randint(0, config.vocab_size - 1, size=[batch_size] * len(config._attrnames), dtype=torch.long)  # batch of 2 random integers from 0 to vocabulary length-1
attention_mask    = torch.zeros([batch_size] + [input1.shape[-2]] * (len(config._attrnames)-3))  # tensor of size 1x64 with 0s
 
__output__        = m(input1, attention_mask=attention_mask)

